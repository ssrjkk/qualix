"""
Contract тесты — два уровня:
1. JSON Schema контракты (без внешних зависимостей, всегда запускаются)
2. Pact consumer-driven контракты (если установлен pact-python)

JSON Schema contracts — лёгкая альтернатива Pact для команд без отдельного broker.
Контракты описывают что именно consumer ожидает от provider.
"""

from __future__ import annotations

from typing import Any

import pytest
from httpx import AsyncClient

# ── JSON Schema контракты (Consumer perspective) ──────────────────────────────
# Описываем что QA Sentinel ожидает от User Service API

CONTRACTS: dict[str, dict] = {
    "user_response": {
        "type": "object",
        "required": ["id", "username", "email", "is_active", "created_at"],
        "properties": {
            "id": {"type": "integer", "minimum": 1},
            "username": {"type": "string", "minLength": 2},
            "email": {"type": "string", "pattern": r".+@.+\..+"},
            "is_active": {"type": "boolean"},
            "created_at": {"type": "string"},
        },
        "additionalProperties": True,
        # Контракт: поля которых НЕ ДОЛЖНО быть в ответе
        "not_allowed_fields": ["password", "hashed_password"],
    },
    "user_list_response": {
        "type": "object",
        "required": ["items", "total", "limit", "offset"],
        "properties": {
            "items": {"type": "array"},
            "total": {"type": "integer", "minimum": 0},
            "limit": {"type": "integer", "minimum": 1},
            "offset": {"type": "integer", "minimum": 0},
        },
    },
    "token_response": {
        "type": "object",
        "required": ["access_token", "token_type"],
        "properties": {
            "access_token": {"type": "string", "minLength": 10},
            "token_type": {"type": "string", "enum": ["bearer"]},
        },
    },
    "error_response": {
        "type": "object",
        "required": ["detail"],
        "properties": {
            "detail": {"type": "string"},
        },
    },
}


def _validate_contract(data: Any, contract_name: str) -> None:
    """Валидируем данные против именованного контракта."""
    contract = CONTRACTS[contract_name]
    assert isinstance(data, dict), f"Expected dict, got {type(data)}"

    for field in contract.get("required", []):
        assert field in data, (
            f"Contract '{contract_name}': required field '{field}' missing. "
            f"Got: {list(data.keys())}"
        )

    for field in contract.get("not_allowed_fields", []):
        assert field not in data, (
            f"Contract '{contract_name}': field '{field}' MUST NOT be in response "
            f"(security leak). Got: {list(data.keys())}"
        )

    for field, spec in contract.get("properties", {}).items():
        if field not in data:
            continue
        value = data[field]
        expected_type = spec.get("type")
        if expected_type == "integer":
            assert isinstance(value, int), (
                f"Contract '{contract_name}': field '{field}' must be int, got {type(value)}"
            )
            if "minimum" in spec:
                assert value >= spec["minimum"], (
                    f"Contract '{contract_name}': '{field}'={value} < minimum {spec['minimum']}"
                )
        elif expected_type == "string":
            assert isinstance(value, str), (
                f"Contract '{contract_name}': field '{field}' must be str, got {type(value)}"
            )
            if "minLength" in spec:
                assert len(value) >= spec["minLength"], (
                    f"Contract '{contract_name}': '{field}' too short"
                )
            if "enum" in spec:
                assert value in spec["enum"], (
                    f"Contract '{contract_name}': '{field}'='{value}' not in {spec['enum']}"
                )
        elif expected_type == "boolean":
            assert isinstance(value, bool), (
                f"Contract '{contract_name}': field '{field}' must be bool, got {type(value)}"
            )
        elif expected_type == "array":
            assert isinstance(value, list), (
                f"Contract '{contract_name}': field '{field}' must be list, got {type(value)}"
            )


# ── Consumer contract тесты ───────────────────────────────────────────────────


@pytest.mark.contract
class TestUserServiceContract:
    """
    Consumer (QA Sentinel) проверяет что Provider (User Service)
    соответствует ожидаемому контракту.
    """

    async def test_create_user_contract(self, client: AsyncClient) -> None:
        """POST /api/v1/users → должен соответствовать user_response контракту."""
        import uuid

        uid = uuid.uuid4().hex[:8]
        resp = await client.post(
            "/api/v1/users",
            json={
                "username": f"contract_{uid}",
                "email": f"c_{uid}@test.com",
                "password": "ContractPass1!",
            },
        )
        assert resp.status_code == 201
        _validate_contract(resp.json(), "user_response")

    async def test_get_user_contract(self, client: AsyncClient, auth_headers: dict) -> None:
        """GET /api/v1/users/{id} → user_response контракт."""
        import uuid

        uid = uuid.uuid4().hex[:8]
        create = await client.post(
            "/api/v1/users",
            json={
                "username": f"cget_{uid}",
                "email": f"cget_{uid}@test.com",
                "password": "ContractPass1!",
            },
        )
        user_id = create.json()["id"]
        resp = await client.get(f"/api/v1/users/{user_id}", headers=auth_headers)
        assert resp.status_code == 200
        _validate_contract(resp.json(), "user_response")

    async def test_list_users_contract(self, client: AsyncClient, auth_headers: dict) -> None:
        """GET /api/v1/users → user_list_response контракт."""
        resp = await client.get("/api/v1/users", headers=auth_headers)
        assert resp.status_code == 200
        _validate_contract(resp.json(), "user_list_response")
        # Каждый элемент тоже должен соответствовать контракту
        for item in resp.json()["items"]:
            _validate_contract(item, "user_response")

    async def test_login_contract(self, client: AsyncClient) -> None:
        """POST /api/v1/auth/login → token_response контракт."""
        resp = await client.post(
            "/api/v1/auth/login",
            json={"username": "test_user", "password": "test_pass"},
        )
        assert resp.status_code == 200
        _validate_contract(resp.json(), "token_response")

    async def test_not_found_error_contract(self, client: AsyncClient, auth_headers: dict) -> None:
        """404 ответ должен соответствовать error_response контракту."""
        resp = await client.get("/api/v1/users/999999999", headers=auth_headers)
        assert resp.status_code == 404
        _validate_contract(resp.json(), "error_response")

    async def test_conflict_error_contract(self, client: AsyncClient) -> None:
        """409 ответ должен соответствовать error_response контракту."""
        import uuid

        uid = uuid.uuid4().hex[:8]
        payload = {
            "username": f"dup_{uid}",
            "email": f"dup_{uid}@test.com",
            "password": "ContractPass1!",
        }
        await client.post("/api/v1/users", json=payload)
        resp = await client.post("/api/v1/users", json=payload)
        assert resp.status_code == 409
        _validate_contract(resp.json(), "error_response")

    async def test_validation_error_contract(self, client: AsyncClient) -> None:
        """422 от FastAPI — проверяем что поле 'detail' присутствует."""
        resp = await client.post("/api/v1/users", json={})
        assert resp.status_code == 422
        data = resp.json()
        assert "detail" in data  # FastAPI validation error format
        assert isinstance(data["detail"], list)  # список ошибок валидации

    async def test_no_password_leak_in_any_response(
        self, client: AsyncClient, auth_headers: dict
    ) -> None:
        """
        Security контракт: ни один response не должен содержать пароль.
        Проверяем рекурсивно весь JSON.
        """
        import uuid

        uid = uuid.uuid4().hex[:8]
        await client.post(
            "/api/v1/users",
            json={
                "username": f"sec_{uid}",
                "email": f"sec_{uid}@test.com",
                "password": "SecretPass1!",
            },
        )
        resp = await client.get("/api/v1/users", headers=auth_headers)
        body_str = resp.text
        assert "SecretPass1!" not in body_str
        assert "hashed_password" not in body_str


@pytest.mark.contract
class TestContractFileExists:
    """Убеждаемся что контракты задокументированы в файле."""

    def test_contracts_dict_not_empty(self) -> None:
        assert len(CONTRACTS) >= 4

    def test_all_required_contracts_defined(self) -> None:
        required = {"user_response", "user_list_response", "token_response", "error_response"}
        missing = required - set(CONTRACTS.keys())
        assert not missing, f"Missing contracts: {missing}"

    def test_user_response_has_security_constraints(self) -> None:
        contract = CONTRACTS["user_response"]
        assert "not_allowed_fields" in contract
        assert "password" in contract["not_allowed_fields"]
        assert "hashed_password" in contract["not_allowed_fields"]
