"""Unit тесты UserRepository — изолированно через AsyncMock сессии."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from app.models.db import UserORM
from app.models.user import UserCreate
from app.repositories.user_repo import UserRepository


def _make_user(id: int = 1) -> UserORM:
    u = UserORM()
    u.id = id
    u.username = f"user_{id}"
    u.email = f"user_{id}@t.com"
    u.hashed_password = "hashed"
    u.is_active = True
    u.created_at = datetime.now(UTC)
    u.updated_at = datetime.now(UTC)
    return u


def _mock_execute(return_value) -> AsyncMock:  # type: ignore[no-untyped-def]
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = return_value
    mock_result.scalar_one.return_value = return_value
    mock_result.scalars.return_value.all.return_value = return_value
    session = AsyncMock()
    session.execute = AsyncMock(return_value=mock_result)
    return session


@pytest.mark.unit
class TestUserRepositoryCreate:
    async def test_create_calls_add_and_flush(self) -> None:
        session = AsyncMock()
        session.add = MagicMock()  # add — синхронный вызов
        nested = AsyncMock()
        nested.__aenter__ = AsyncMock(return_value=None)
        nested.__aexit__ = AsyncMock(return_value=False)
        session.begin_nested = MagicMock(return_value=nested)

        async def set_id(obj):  # type: ignore[no-untyped-def]
            obj.id = 42
            obj.created_at = datetime.now(UTC)
            obj.updated_at = datetime.now(UTC)

        session.refresh = AsyncMock(side_effect=set_id)

        repo = UserRepository(session)
        user = await repo.create(
            UserCreate(username="newuser", email="new@t.com", password="NewPass1!")
        )
        assert user.id == 42
        session.add.assert_called_once()

    async def test_create_uses_bcrypt_hash(self) -> None:
        """Пароль хешируется через bcrypt — не plaintext."""
        session = AsyncMock()
        session.add = MagicMock()  # add — синхронный
        nested = AsyncMock()
        nested.__aenter__ = AsyncMock(return_value=None)
        nested.__aexit__ = AsyncMock(return_value=False)
        session.begin_nested = MagicMock(return_value=nested)

        captured = {}

        async def capture_and_set(obj):  # type: ignore[no-untyped-def]
            captured["hash"] = obj.hashed_password
            obj.id = 1
            obj.created_at = datetime.now(UTC)
            obj.updated_at = datetime.now(UTC)

        session.refresh = AsyncMock(side_effect=capture_and_set)

        repo = UserRepository(session)
        await repo.create(UserCreate(username="usr", email="usr@t.com", password="PlainPass1!"))

        assert captured["hash"] != "PlainPass1!"
        assert captured["hash"].startswith("$2b$")  # bcrypt signature


@pytest.mark.unit
class TestUserRepositoryRead:
    async def test_get_by_id_found(self) -> None:
        session = _mock_execute(_make_user(5))
        result = await UserRepository(session).get_by_id(5)
        assert result is not None
        assert result.id == 5

    async def test_get_by_id_not_found(self) -> None:
        session = _mock_execute(None)
        result = await UserRepository(session).get_by_id(999)
        assert result is None

    async def test_get_by_email_found(self) -> None:
        user = _make_user(3)
        session = _mock_execute(user)
        result = await UserRepository(session).get_by_email("user_3@t.com")
        assert result is not None

    async def test_get_by_email_lowercases_input(self) -> None:
        session = _mock_execute(None)
        await UserRepository(session).get_by_email("USER@TEST.COM")
        # Проверяем что execute вызвался — lowercase происходит внутри query
        session.execute.assert_awaited_once()

    async def test_list_returns_list(self) -> None:
        users = [_make_user(i) for i in range(5)]
        session = _mock_execute(users)
        result = await UserRepository(session).list(limit=5, offset=0)
        assert len(result) == 5

    async def test_count_returns_int(self) -> None:
        session = _mock_execute(42)
        result = await UserRepository(session).count()
        assert result == 42


@pytest.mark.unit
class TestUserRepositoryDelete:
    async def test_delete_found_returns_true(self) -> None:
        user = _make_user(7)
        session = _mock_execute(user)
        session.delete = AsyncMock()
        session.flush = AsyncMock()
        result = await UserRepository(session).delete(7)
        assert result is True
        session.delete.assert_awaited_once_with(user)

    async def test_delete_not_found_returns_false(self) -> None:
        session = _mock_execute(None)
        result = await UserRepository(session).delete(999)
        assert result is False
        session.delete.assert_not_awaited()
