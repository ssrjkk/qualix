"""Тесты Auth API — dummyjson.com/auth/login"""
from __future__ import annotations

import pytest
import httpx
from app.external.dummyjson import DummyJSONClient


@pytest.mark.api
class TestLogin:

    async def test_valid_credentials_returns_tokens(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.login("emilys", "emilyspass")
        assert "accessToken" in result
        assert "refreshToken" in result
        assert len(result["accessToken"]) > 20

    async def test_login_returns_user_info(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.login("emilys", "emilyspass")
        assert "id" in result
        assert "username" in result
        assert "email" in result
        assert "@" in result["email"]

    async def test_invalid_credentials_raises(self, dummyjson: DummyJSONClient) -> None:
        with pytest.raises(httpx.HTTPStatusError) as exc:
            await dummyjson.login("wronguser", "wrongpassword")
        assert exc.value.response.status_code == 400

    async def test_access_token_is_jwt_like(self, dummyjson: DummyJSONClient) -> None:
        """accessToken должен быть JWT (три части разделённые точкой)."""
        result = await dummyjson.login("emilys", "emilyspass")
        parts = result["accessToken"].split(".")
        assert len(parts) == 3, "accessToken is not a valid JWT format"

    async def test_both_tokens_different(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.login("emilys", "emilyspass")
        assert result["accessToken"] != result["refreshToken"]
