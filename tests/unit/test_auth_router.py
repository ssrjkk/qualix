"""Unit тесты auth router — прямые вызовы с AsyncMock."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from app.api import auth as auth_module
from app.models.db import UserORM


def _make_user(email: str = "u@t.com", password: str = "Pass1!") -> UserORM:
    from app.security import hash_password

    u = UserORM()
    u.id = 1
    u.username = "testuser"
    u.email = email
    u.hashed_password = hash_password(password)
    u.is_active = True
    u.created_at = datetime.now(UTC)
    u.updated_at = datetime.now(UTC)
    return u


def _mock_settings(secret: str = "test-secret-key-32chars!") -> MagicMock:
    s = MagicMock()
    s.secret_key = secret
    s.access_token_expire_minutes = 30
    return s


@pytest.mark.unit
class TestLoginRouter:
    async def test_hardcoded_test_user_returns_token(self) -> None:
        mock_db = AsyncMock()
        result = await auth_module.login(
            data=auth_module.LoginRequest(username="test_user", password="test_pass"),
            db=mock_db,
            settings=_mock_settings(),
        )
        assert result.access_token
        assert result.token_type == "bearer"

    async def test_hardcoded_admin_returns_token(self) -> None:
        mock_db = AsyncMock()
        result = await auth_module.login(
            data=auth_module.LoginRequest(username="admin", password="admin_pass"),
            db=mock_db,
            settings=_mock_settings(),
        )
        assert result.access_token

    async def test_db_user_correct_password_returns_token(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.auth.UserRepository") as repo:
            repo.return_value.get_by_email = AsyncMock(
                return_value=_make_user("db@t.com", "DbPass1!")
            )
            result = await auth_module.login(
                data=auth_module.LoginRequest(username="db@t.com", password="DbPass1!"),
                db=mock_db,
                settings=_mock_settings(),
            )
        assert result.access_token

    async def test_db_user_not_found_raises_401(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.auth.UserRepository") as repo:
            repo.return_value.get_by_email = AsyncMock(return_value=None)
            with pytest.raises(HTTPException) as exc:
                await auth_module.login(
                    data=auth_module.LoginRequest(username="ghost@t.com", password="Pass1!"),
                    db=mock_db,
                    settings=_mock_settings(),
                )
        assert exc.value.status_code == 401

    async def test_db_user_wrong_password_raises_401(self) -> None:
        mock_db = AsyncMock()
        with patch("app.api.auth.UserRepository") as repo:
            repo.return_value.get_by_email = AsyncMock(
                return_value=_make_user("u@t.com", "RealPass1!")
            )
            with pytest.raises(HTTPException) as exc:
                await auth_module.login(
                    data=auth_module.LoginRequest(username="u@t.com", password="WrongPass1!"),
                    db=mock_db,
                    settings=_mock_settings(),
                )
        assert exc.value.status_code == 401

    async def test_token_grants_db_user_access(self) -> None:
        """Token созданный для DB юзера валидируется через _verify_token."""
        mock_db = AsyncMock()
        with patch("app.api.auth.UserRepository") as repo:
            repo.return_value.get_by_email = AsyncMock(return_value=_make_user("u@t.com", "Pass1!"))
            resp = await auth_module.login(
                data=auth_module.LoginRequest(username="u@t.com", password="Pass1!"),
                db=mock_db,
                settings=_mock_settings(),
            )
        # Верифицируем полученный токен
        username = auth_module._verify_token(resp.access_token, "test-secret-key-32chars!")
        assert username == "testuser"
