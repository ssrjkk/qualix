"""
Root conftest.py

Два режима:
  Docker доступен → testcontainers (Postgres + Redis)
  иначе           → SQLite in-memory (без Docker)
"""

from __future__ import annotations

import socket
from collections.abc import AsyncGenerator, Generator
from typing import Any

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from app.config import Settings
from app.models.db import Base

# ── Docker detection ──────────────────────────────────────────────────────────


def _docker_available() -> bool:
    if not hasattr(socket, "AF_UNIX"):
        return False
    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect("/var/run/docker.sock")
        s.close()
        return True
    except OSError:
        return False


DOCKER_UP = _docker_available()


# ── Settings ──────────────────────────────────────────────────────────────────

if "DATABASE_URL" in __import__("os").environ:

    @pytest.fixture(scope="session")
    def test_settings() -> Settings:  # type: ignore
        return Settings(
            database_url=__import__("os").environ["DATABASE_URL"],
            redis_url=__import__("os").environ.get("REDIS_URL", "redis://localhost:6379/0"),
            environment="test",
            secret_key="test-secret-key-32chars!",
        )

elif DOCKER_UP:

    @pytest.fixture(scope="session")
    def _pg() -> Generator:  # type: ignore
        from testcontainers.postgres import PostgresContainer

        with PostgresContainer("postgres:16-alpine") as pg:
            yield pg

    @pytest.fixture(scope="session")
    def _redis() -> Generator:  # type: ignore
        from testcontainers.redis import RedisContainer

        with RedisContainer("redis:7-alpine") as r:
            yield r

    @pytest.fixture(scope="session")
    def test_settings(_pg, _redis) -> Settings:  # noqa: PT019  # type: ignore
        url = _pg.get_connection_url().replace("postgresql://", "postgresql+asyncpg://")
        redis_url = f"redis://{_redis.get_container_host_ip()}:{_redis.get_exposed_port(6379)}/0"
        return Settings(
            database_url=url,
            redis_url=redis_url,
            environment="test",
            secret_key="test-secret-key-32chars!",
        )
else:

    @pytest.fixture(scope="session")
    def test_settings() -> Settings:  # type: ignore
        return Settings(
            database_url="sqlite+aiosqlite:///./test_sentinel.db",
            redis_url="redis://localhost:6379/0",
            environment="test",
            secret_key="test-secret-key-32chars!",
        )


# ── App (session scope) ───────────────────────────────────────────────────────


@pytest.fixture(scope="session")
def app(test_settings: Settings) -> Any:
    from app.main import create_app

    return create_app(settings=test_settings)


# ── HTTP client с lifespan ────────────────────────────────────────────────────


@pytest_asyncio.fixture(scope="session")
async def client(app: Any) -> AsyncGenerator[AsyncClient, None]:
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
        ) as c:
            yield c


# ── Auth fixtures ─────────────────────────────────────────────────────────────


@pytest_asyncio.fixture
async def auth_headers(client: AsyncClient) -> dict[str, str]:
    resp = await client.post(
        "/api/v1/auth/login",
        json={"username": "test_user", "password": "test_pass"},
    )
    assert resp.status_code == 200, f"Auth failed: {resp.text}"
    return {"Authorization": f"Bearer {resp.json()['access_token']}"}


@pytest_asyncio.fixture
async def admin_headers(client: AsyncClient) -> dict[str, str]:
    resp = await client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "admin_pass"},
    )
    assert resp.status_code == 200
    return {"Authorization": f"Bearer {resp.json()['access_token']}"}


# ── DB session для integration тестов ────────────────────────────────────────


@pytest_asyncio.fixture(scope="session")
async def db_engine(test_settings: Settings) -> AsyncGenerator[AsyncEngine, None]:
    # engine уже создан create_app, берём его
    from app.dependencies import get_engine

    # убедимся что приложение инициализировано
    engine = get_engine(test_settings)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine


@pytest_asyncio.fixture
async def db_session(db_engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
    """Транзакция с rollback после каждого теста — нет dirty state."""
    connection = await db_engine.connect()
    transaction = await connection.begin()
    factory = async_sessionmaker(bind=connection, expire_on_commit=False, autoflush=False)
    async with factory() as session:
        yield session
    await transaction.rollback()
    await connection.close()
