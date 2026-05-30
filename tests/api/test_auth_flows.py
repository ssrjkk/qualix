"""
API тесты для auth flows — покрываем DB-path логин и edge cases.
"""

from __future__ import annotations

import uuid

import pytest
from httpx import AsyncClient


@pytest.mark.api
class TestAuthDBPath:
    """
    Тесты логина через реального DB-пользователя.
    Покрывают строки auth.py:71-78 (не hardcoded тест-юзеры).
    """

    async def test_login_as_real_db_user(self, client: AsyncClient) -> None:
        """Создаём юзера, логинимся через email — покрывает DB путь auth.py:63-78."""
        uid = uuid.uuid4().hex[:8]
        email = f"real_{uid}@db.com"
        password = "RealPass1!"

        # Создаём пользователя
        create = await client.post(
            "/api/v1/users",
            json={"username": f"real_{uid}", "email": email, "password": password},
        )
        assert create.status_code == 201

        # Логинимся через email как username — покрывает строки 63-78
        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": email, "password": password},
        )
        assert resp.status_code == 200
        assert "access_token" in resp.json()

    async def test_login_db_user_wrong_password(self, client: AsyncClient) -> None:
        """DB юзер + неверный пароль → 401. Покрывает auth.py:74-75."""
        uid = uuid.uuid4().hex[:8]
        email = f"wrong_{uid}@db.com"

        await client.post(
            "/api/v1/users",
            json={"username": f"wrong_{uid}", "email": email, "password": "CorrectPass1!"},
        )

        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": email, "password": "WrongPass1!"},
        )
        assert resp.status_code == 401

    async def test_login_nonexistent_db_user(self, client: AsyncClient) -> None:
        """Email не существует в DB → 401. Покрывает auth.py:71-72."""
        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": "nobody_xyz@notexist.com", "password": "AnyPass1!"},
        )
        assert resp.status_code == 401

    async def test_expired_token_returns_401(self, client: AsyncClient) -> None:
        """Expired token → 401. Покрывает _verify_token line 47."""
        from app.api.auth import _create_token

        expired = _create_token("test_user", "test-secret-key-32chars!", expires_minutes=-5)
        resp = await client.get(
            "/api/v1/users",
            headers={"Authorization": f"Bearer {expired}"},
        )
        assert resp.status_code == 401

    async def test_token_with_wrong_secret_returns_401(self, client: AsyncClient) -> None:
        """Token подписан другим секретом → 401."""
        from app.api.auth import _create_token

        bad_token = _create_token("test_user", "completely-different-secret-key!")
        resp = await client.get(
            "/api/v1/users",
            headers={"Authorization": f"Bearer {bad_token}"},
        )
        assert resp.status_code == 401


@pytest.mark.api
class TestUsersAPICoverage:
    """
    Целевые тесты для покрытия непокрытых строк users.py.
    """

    async def test_create_user_success_path(self, client: AsyncClient) -> None:
        """Явно проверяем успешный create — users.py:24 (return UserResponse)."""
        uid = uuid.uuid4().hex[:8]
        resp = await client.post(
            "/api/v1/users",
            json={
                "username": f"cov_{uid}",
                "email": f"cov_{uid}@test.com",
                "password": "CovPass1!",
            },
        )
        assert resp.status_code == 201
        data = resp.json()
        # Проверяем все поля UserResponse
        assert isinstance(data["id"], int)
        assert data["username"] == f"cov_{uid}"
        assert data["email"] == f"cov_{uid}@test.com"
        assert isinstance(data["is_active"], bool)
        assert "created_at" in data

    async def test_create_duplicate_triggers_409(self, client: AsyncClient) -> None:
        """IntegrityError → HTTPException 409 — users.py:25-26."""
        uid = uuid.uuid4().hex[:8]
        payload = {
            "username": f"dup_{uid}",
            "email": f"dup_{uid}@test.com",
            "password": "DupPass1!",
        }
        r1 = await client.post("/api/v1/users", json=payload)
        assert r1.status_code == 201
        r2 = await client.post("/api/v1/users", json=payload)
        assert r2.status_code == 409
        assert "already" in r2.json()["detail"].lower()

    async def test_list_users_returns_response(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        """list_users return — users.py:39."""
        resp = await client.get("/api/v1/users", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        # Проверяем все поля UserListResponse
        assert "items" in data
        assert "total" in data
        assert "limit" in data
        assert "offset" in data
        assert isinstance(data["items"], list)
        assert data["limit"] == 20  # default
        assert data["offset"] == 0  # default

    async def test_get_user_found_path(self, client: AsyncClient, auth_headers: dict) -> None:
        """get_user happy path — users.py:55-57."""
        uid = uuid.uuid4().hex[:8]
        create = await client.post(
            "/api/v1/users",
            json={
                "username": f"getok_{uid}",
                "email": f"getok_{uid}@test.com",
                "password": "GetPass1!",
            },
        )
        user_id = create.json()["id"]
        resp = await client.get(f"/api/v1/users/{user_id}", headers=auth_headers)
        assert resp.status_code == 200
        assert resp.json()["id"] == user_id

    async def test_get_user_not_found_path(self, client: AsyncClient, auth_headers: dict) -> None:
        """get_user 404 — users.py:55-56 (not found branch)."""
        resp = await client.get("/api/v1/users/999888777", headers=auth_headers)
        assert resp.status_code == 404
        assert "not found" in resp.json()["detail"].lower()

    async def test_delete_user_not_found_path(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        """delete_user 404 — users.py:68-69."""
        resp = await client.delete("/api/v1/users/999888777", headers=auth_headers)
        assert resp.status_code == 404
        assert "not found" in resp.json()["detail"].lower()

    async def test_delete_user_success_path(self, client: AsyncClient, auth_headers: dict) -> None:
        """delete_user 204 — users.py полный happy path."""
        uid = uuid.uuid4().hex[:8]
        create = await client.post(
            "/api/v1/users",
            json={
                "username": f"del_{uid}",
                "email": f"del_{uid}@test.com",
                "password": "DelPass1!",
            },
        )
        user_id = create.json()["id"]
        resp = await client.delete(f"/api/v1/users/{user_id}", headers=auth_headers)
        assert resp.status_code == 204
