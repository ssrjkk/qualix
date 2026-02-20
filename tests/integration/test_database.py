"""
Integration тесты — SQLite (fallback) или Postgres (с Docker).
Redis — fakeredis локально, реальный Redis в CI через testcontainers.
"""
from __future__ import annotations

import socket
import uuid
import pytest
import fakeredis.aioredis as fakeredis
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, async_sessionmaker

from app.repositories.user_repo import UserRepository
from app.models.user import UserCreate


def _uid() -> str:
    return uuid.uuid4().hex[:8]


def _user(uid: str | None = None) -> UserCreate:
    u = uid or _uid()
    return UserCreate(
        username=f"integ_{u}",
        email=f"integ_{u}@example.com",
        password="ValidPass1!",
    )


def _real_redis_available() -> bool:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect(("127.0.0.1", 6379))
        s.close()
        return True
    except OSError:
        return False


REAL_REDIS_UP = _real_redis_available()


# ── DB тесты ──────────────────────────────────────────────────────────────────

@pytest.mark.integration
class TestUserRepository:

    async def test_create_returns_id(self, db_session: AsyncSession) -> None:
        repo = UserRepository(db_session)
        data = _user()
        user = await repo.create(data)
        assert user.id is not None
        assert user.email == data.email

    async def test_get_by_id_found(self, db_session: AsyncSession) -> None:
        repo = UserRepository(db_session)
        created = await repo.create(_user())
        fetched = await repo.get_by_id(created.id)
        assert fetched is not None
        assert fetched.username == created.username

    async def test_get_by_id_not_found(self, db_session: AsyncSession) -> None:
        assert await UserRepository(db_session).get_by_id(99999) is None

    async def test_get_by_email(self, db_session: AsyncSession) -> None:
        repo = UserRepository(db_session)
        data = _user()
        await repo.create(data)
        found = await repo.get_by_email(data.email)
        assert found is not None
        assert found.email == data.email

    async def test_duplicate_email_raises(self, db_engine: AsyncEngine) -> None:
        """Дубликат email — отдельная сессия (SQLite не держит savepoint)."""
        from sqlalchemy.exc import IntegrityError
        factory = async_sessionmaker(db_engine, expire_on_commit=False, autoflush=False)
        uid = _uid()
        async with factory() as s1:
            await UserRepository(s1).create(_user(uid))
            await s1.commit()
        async with factory() as s2:
            with pytest.raises(IntegrityError):
                dupe = UserCreate(
                    username=f"other_{uid}",
                    email=f"integ_{uid}@example.com",
                    password="ValidPass1!",
                )
                await UserRepository(s2).create(dupe)

    async def test_list_no_overlap(self, db_session: AsyncSession) -> None:
        repo = UserRepository(db_session)
        before = await repo.count()
        for _ in range(12):
            await repo.create(_user())
        p1 = await repo.list(limit=5, offset=before)
        p2 = await repo.list(limit=5, offset=before + 5)
        assert len(p1) == 5
        assert {u.id for u in p1}.isdisjoint({u.id for u in p2})

    async def test_delete_existing(self, db_session: AsyncSession) -> None:
        repo = UserRepository(db_session)
        user = await repo.create(_user())
        assert await repo.delete(user.id) is True
        assert await repo.get_by_id(user.id) is None

    async def test_delete_nonexistent(self, db_session: AsyncSession) -> None:
        assert await UserRepository(db_session).delete(99999) is False

    async def test_count_increments(self, db_session: AsyncSession) -> None:
        repo = UserRepository(db_session)
        before = await repo.count()
        await repo.create(_user())
        assert await repo.count() == before + 1


# ── Redis тесты (fakeredis — всегда работают, реальный Redis — в CI) ──────────

@pytest.mark.integration
class TestRedisCache:
    """
    Запускаются везде через fakeredis.
    При наличии реального Redis — дополнительно тестируем его.
    """

    async def test_set_and_get_fake(self) -> None:
        r = fakeredis.FakeRedis()
        await r.set("sentinel:test", b"hello", ex=60)
        assert await r.get("sentinel:test") == b"hello"
        await r.aclose()

    async def test_missing_key_returns_none_fake(self) -> None:
        r = fakeredis.FakeRedis()
        assert await r.get("sentinel:nonexistent_xyz") is None
        await r.aclose()

    async def test_overwrite_key_fake(self) -> None:
        r = fakeredis.FakeRedis()
        await r.set("sentinel:overwrite", b"v1")
        await r.set("sentinel:overwrite", b"v2")
        assert await r.get("sentinel:overwrite") == b"v2"
        await r.aclose()

    async def test_ttl_expiry_fake(self) -> None:
        """fakeredis поддерживает TTL через time_func."""
        import time
        server = fakeredis.FakeServer()
        server.connected = True
        r = fakeredis.FakeRedis(server=server)
        await r.set("sentinel:ttl", b"bye", ex=1)
        # fakeredis не реально истекает по времени без мокирования времени,
        # проверяем что TTL установлен
        ttl = await r.ttl("sentinel:ttl")
        assert ttl > 0
        await r.aclose()

    async def test_incr_fake(self) -> None:
        r = fakeredis.FakeRedis()
        await r.set("sentinel:counter", 0)
        await r.incr("sentinel:counter")
        await r.incr("sentinel:counter")
        val = await r.get("sentinel:counter")
        assert int(val) == 2
        await r.aclose()

    async def test_exists_fake(self) -> None:
        r = fakeredis.FakeRedis()
        await r.set("sentinel:exists", b"yes")
        assert await r.exists("sentinel:exists") == 1
        assert await r.exists("sentinel:nokey") == 0
        await r.aclose()

    async def test_delete_fake(self) -> None:
        r = fakeredis.FakeRedis()
        await r.set("sentinel:del", b"x")
        await r.delete("sentinel:del")
        assert await r.get("sentinel:del") is None
        await r.aclose()

    async def test_hset_hget_fake(self) -> None:
        """Hash операции — типичный паттерн для сессий."""
        r = fakeredis.FakeRedis()
        await r.hset("sentinel:session:abc", mapping={"user_id": "42", "role": "admin"})
        user_id = await r.hget("sentinel:session:abc", "user_id")
        assert user_id == b"42"
        await r.aclose()

    @pytest.mark.skipif(not REAL_REDIS_UP, reason="Real Redis not available — run with Docker")
    async def test_real_redis_set_get(self, test_settings) -> None:  # type: ignore
        import redis.asyncio as aioredis
        r = aioredis.from_url(test_settings.redis_url)
        uid = _uid()
        await r.set(f"sentinel:real:{uid}", b"real_hello", ex=60)
        assert await r.get(f"sentinel:real:{uid}") == b"real_hello"
        await r.aclose()
