"""
API тесты — httpx AsyncClient + factory_boy.
Полное покрытие: happy path, негативные сценарии, auth, pagination.
"""
from __future__ import annotations

import pytest
from httpx import AsyncClient

from tests.factories.user_factory import UserPayloadFactory


# ── Создание пользователя ─────────────────────────────────────────────────────

@pytest.mark.api
class TestCreateUser:

    async def test_201_returns_id_no_password(
        self, client: AsyncClient, user_payload: dict
    ) -> None:
        resp = await client.post("/api/v1/users", json=user_payload)
        assert resp.status_code == 201
        data = resp.json()
        assert "id" in data
        assert "password" not in data
        assert "hashed_password" not in data

    async def test_201_email_normalized_lowercase(self, client: AsyncClient) -> None:
        payload = UserPayloadFactory()
        payload["email"] = payload["email"].upper()
        resp = await client.post("/api/v1/users", json=payload)
        assert resp.status_code == 201
        assert resp.json()["email"] == payload["email"].lower()

    async def test_409_duplicate_email(self, client: AsyncClient, user_payload: dict) -> None:
        await client.post("/api/v1/users", json=user_payload)
        resp = await client.post("/api/v1/users", json=user_payload)
        assert resp.status_code == 409

    @pytest.mark.parametrize("missing_field", ["username", "email", "password"])
    async def test_422_missing_required_field(
        self, client: AsyncClient, user_payload: dict, missing_field: str
    ) -> None:
        del user_payload[missing_field]
        resp = await client.post("/api/v1/users", json=user_payload)
        assert resp.status_code == 422

    @pytest.mark.parametrize("bad_email", [
        "notanemail",
        "missing@",
        "@nodomain.com",
        "a" * 255 + "@x.com",
        "two@@domain.com",
    ])
    async def test_422_invalid_email(self, client: AsyncClient, bad_email: str) -> None:
        payload = UserPayloadFactory(email=bad_email)
        resp = await client.post("/api/v1/users", json=payload)
        assert resp.status_code == 422

    @pytest.mark.parametrize("trait", ["short_password", "no_upper", "no_digit"])
    async def test_422_invalid_password(self, client: AsyncClient, trait: str) -> None:
        payload = UserPayloadFactory(**{trait: True})
        resp = await client.post("/api/v1/users", json=payload)
        assert resp.status_code == 422

    async def test_422_username_too_short(self, client: AsyncClient) -> None:
        resp = await client.post(
            "/api/v1/users",
            json=UserPayloadFactory(username="x"),
        )
        assert resp.status_code == 422


# ── Получение пользователя ────────────────────────────────────────────────────

@pytest.mark.api
class TestGetUser:

    async def test_200_get_existing(
        self, client: AsyncClient, auth_headers: dict, created_user: dict
    ) -> None:
        resp = await client.get(
            f"/api/v1/users/{created_user['id']}", headers=auth_headers
        )
        assert resp.status_code == 200
        assert resp.json()["id"] == created_user["id"]

    async def test_200_response_shape(
        self, client: AsyncClient, auth_headers: dict, created_user: dict
    ) -> None:
        resp = await client.get(
            f"/api/v1/users/{created_user['id']}", headers=auth_headers
        )
        data = resp.json()
        assert set(data.keys()) >= {"id", "username", "email", "is_active", "created_at"}
        assert "password" not in data
        assert "hashed_password" not in data

    async def test_404_nonexistent(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        resp = await client.get("/api/v1/users/999999999", headers=auth_headers)
        assert resp.status_code == 404

    async def test_401_no_token(self, client: AsyncClient) -> None:
        resp = await client.get("/api/v1/users/1")
        assert resp.status_code == 401

    async def test_401_bad_token(self, client: AsyncClient) -> None:
        resp = await client.get(
            "/api/v1/users/1",
            headers={"Authorization": "Bearer totally.fake.token"},
        )
        assert resp.status_code == 401

    async def test_401_malformed_header(self, client: AsyncClient) -> None:
        resp = await client.get(
            "/api/v1/users/1",
            headers={"Authorization": "NotBearer abc"},
        )
        assert resp.status_code == 401


# ── Список пользователей ──────────────────────────────────────────────────────

@pytest.mark.api
class TestListUsers:

    async def test_200_default_pagination(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        resp = await client.get("/api/v1/users", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert "items" in data and "total" in data
        assert "limit" in data and "offset" in data

    @pytest.mark.parametrize("limit,offset", [(1, 0), (5, 0), (10, 5), (20, 0)])
    async def test_200_pagination_respects_limit(
        self, client: AsyncClient, auth_headers: dict, limit: int, offset: int
    ) -> None:
        resp = await client.get(
            "/api/v1/users",
            params={"limit": limit, "offset": offset},
            headers=auth_headers,
        )
        assert resp.status_code == 200
        assert len(resp.json()["items"]) <= limit

    async def test_422_limit_over_100(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        resp = await client.get(
            "/api/v1/users", params={"limit": 101}, headers=auth_headers
        )
        assert resp.status_code == 422

    async def test_422_negative_offset(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        resp = await client.get(
            "/api/v1/users", params={"offset": -1}, headers=auth_headers
        )
        assert resp.status_code == 422

    async def test_401_unauthenticated(self, client: AsyncClient) -> None:
        resp = await client.get("/api/v1/users")
        assert resp.status_code == 401


# ── Удаление ─────────────────────────────────────────────────────────────────

@pytest.mark.api
class TestDeleteUser:

    async def test_204_delete_existing(
        self, client: AsyncClient, auth_headers: dict, created_user: dict
    ) -> None:
        resp = await client.delete(
            f"/api/v1/users/{created_user['id']}", headers=auth_headers
        )
        assert resp.status_code == 204

    async def test_404_after_delete(
        self, client: AsyncClient, auth_headers: dict, created_user: dict
    ) -> None:
        uid = created_user["id"]
        await client.delete(f"/api/v1/users/{uid}", headers=auth_headers)
        resp = await client.get(f"/api/v1/users/{uid}", headers=auth_headers)
        assert resp.status_code == 404

    async def test_404_nonexistent(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        resp = await client.delete("/api/v1/users/999999999", headers=auth_headers)
        assert resp.status_code == 404

    async def test_401_unauthenticated(
        self, client: AsyncClient, created_user: dict
    ) -> None:
        resp = await client.delete(f"/api/v1/users/{created_user['id']}")
        assert resp.status_code == 401


# ── Auth ──────────────────────────────────────────────────────────────────────

@pytest.mark.api
class TestAuth:

    async def test_200_valid_login_returns_token(self, client: AsyncClient) -> None:
        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": "test_user", "password": "test_pass"},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert len(data["access_token"]) > 20

    async def test_200_token_grants_access(self, client: AsyncClient) -> None:
        login = await client.post(
            "/api/v1/auth/login",
            json={"username": "test_user", "password": "test_pass"},
        )
        token = login.json()["access_token"]
        resp = await client.get(
            "/api/v1/users", headers={"Authorization": f"Bearer {token}"}
        )
        assert resp.status_code == 200

    async def test_401_wrong_password(self, client: AsyncClient) -> None:
        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": "test_user", "password": "WRONG"},
        )
        assert resp.status_code == 401

    async def test_401_unknown_user(self, client: AsyncClient) -> None:
        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": "ghost@nobody.com", "password": "pass"},
        )
        assert resp.status_code == 401

    async def test_401_empty_credentials(self, client: AsyncClient) -> None:
        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": "", "password": ""},
        )
        assert resp.status_code == 401


# ── Health ────────────────────────────────────────────────────────────────────

@pytest.mark.api
class TestHealth:

    async def test_200_health(self, client: AsyncClient) -> None:
        resp = await client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"

    async def test_health_env_is_test(self, client: AsyncClient) -> None:
        resp = await client.get("/health")
        assert resp.json()["environment"] == "test"

    async def test_health_no_auth_required(self, client: AsyncClient) -> None:
        """Health endpoint должен быть публичным — для k8s liveness probe."""
        resp = await client.get("/health")
        assert resp.status_code == 200
