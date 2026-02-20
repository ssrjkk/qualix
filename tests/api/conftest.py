"""API layer conftest — фикстуры специфичные для HTTP тестов."""
from __future__ import annotations

import pytest
import pytest_asyncio
from httpx import AsyncClient

from tests.factories.user_factory import UserPayloadFactory


@pytest.fixture
def user_payload() -> dict:
    """Свежий уникальный payload для создания пользователя."""
    return UserPayloadFactory()


@pytest.fixture
def invalid_payloads() -> dict[str, dict]:
    """Набор невалидных payload для негативных тестов."""
    return {
        "invalid_email": UserPayloadFactory(invalid_email=True),
        "short_password": UserPayloadFactory(short_password=True),
        "no_upper": UserPayloadFactory(no_upper=True),
        "no_digit": UserPayloadFactory(no_digit=True),
    }


@pytest_asyncio.fixture
async def created_user(client: AsyncClient, user_payload: dict) -> dict:
    """Создаёт пользователя и возвращает response body."""
    resp = await client.post("/api/v1/users", json=user_payload)
    assert resp.status_code == 201, f"Setup failed: {resp.text}"
    return resp.json()
