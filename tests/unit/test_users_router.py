"""Unit тесты users router — прямые вызовы с AsyncMock зависимостями."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock, patch

import pytest
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.api import users as users_module
from app.models.db import UserORM
from app.models.user import UserCreate, UserListResponse, UserResponse


def _make_user(id: int = 1, username: str = "testuser", email: str = "t@t.com") -> UserORM:
    u = UserORM()
    u.id = id
    u.username = username
    u.email = email
    u.hashed_password = "hashed"
    u.is_active = True
    u.created_at = datetime.now(UTC)
    u.updated_at = datetime.now(UTC)
    return u


@pytest.mark.unit
class TestCreateUserRouter:
    async def test_success_returns_user_response(self) -> None:
        mock_db = AsyncMock()
        mock_user = _make_user()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.create = AsyncMock(return_value=mock_user)
            result = await users_module.create_user(
                data=UserCreate(username="testuser", email="t@t.com", password="TestPass1!"),
                db=mock_db,
            )
        assert isinstance(result, UserResponse)
        assert result.id == 1
        mock_db.commit.assert_awaited_once()

    async def test_integrity_error_raises_409(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.create = AsyncMock(side_effect=IntegrityError("dup", {}, None))
            with pytest.raises(HTTPException) as exc:
                await users_module.create_user(
                    data=UserCreate(username="dup", email="d@t.com", password="TestPass1!"),
                    db=mock_db,
                )
        assert exc.value.status_code == 409

    async def test_response_has_no_password_field(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.create = AsyncMock(return_value=_make_user())
            result = await users_module.create_user(
                data=UserCreate(username="usr", email="usr@t.com", password="TestPass1!"),
                db=mock_db,
            )
        data = result.model_dump()
        assert "password" not in data
        assert "hashed_password" not in data


@pytest.mark.unit
class TestListUsersRouter:
    async def test_returns_list_response(self) -> None:
        mock_db = AsyncMock()
        users = [_make_user(i, f"u{i}", f"u{i}@t.com") for i in range(5)]
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.list = AsyncMock(return_value=users)
            repo.return_value.count = AsyncMock(return_value=5)
            result = await users_module.list_users(
                limit=20, offset=0, db=mock_db, _={"username": "admin"}
            )
        assert isinstance(result, UserListResponse)
        assert result.total == 5
        assert len(result.items) == 5

    async def test_pagination_params_passed_correctly(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.list = AsyncMock(return_value=[])
            repo.return_value.count = AsyncMock(return_value=100)
            result = await users_module.list_users(
                limit=5, offset=10, db=mock_db, _={"username": "admin"}
            )
        assert result.limit == 5
        assert result.offset == 10
        repo.return_value.list.assert_awaited_once_with(limit=5, offset=10)

    async def test_empty_list_returns_valid_response(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.list = AsyncMock(return_value=[])
            repo.return_value.count = AsyncMock(return_value=0)
            result = await users_module.list_users(
                limit=20, offset=0, db=mock_db, _={"username": "admin"}
            )
        assert result.items == []
        assert result.total == 0


@pytest.mark.unit
class TestGetUserRouter:
    async def test_found_returns_user_response(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.get_by_id = AsyncMock(return_value=_make_user(42))
            result = await users_module.get_user(user_id=42, db=mock_db, _={"username": "admin"})
        assert isinstance(result, UserResponse)
        assert result.id == 42

    async def test_not_found_raises_404(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.get_by_id = AsyncMock(return_value=None)
            with pytest.raises(HTTPException) as exc:
                await users_module.get_user(user_id=999, db=mock_db, _={"username": "admin"})
        assert exc.value.status_code == 404
        assert "not found" in exc.value.detail.lower()


@pytest.mark.unit
class TestDeleteUserRouter:
    async def test_success_returns_none(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.delete = AsyncMock(return_value=True)
            result = await users_module.delete_user(user_id=1, db=mock_db, _={"username": "admin"})
        assert result is None
        mock_db.commit.assert_awaited_once()

    async def test_not_found_raises_404(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.users.UserRepository") as repo:
            repo.return_value.delete = AsyncMock(return_value=False)
            with pytest.raises(HTTPException) as exc:
                await users_module.delete_user(user_id=999, db=mock_db, _={"username": "admin"})
        assert exc.value.status_code == 404
