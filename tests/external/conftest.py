"""
External API conftest — respx моки для dummyjson.com.

Режимы:
  По умолчанию  → respx (детерминированы, без сети)
  --live-api    → реальный HTTP к dummyjson.com
"""

from __future__ import annotations

import json
from collections.abc import AsyncGenerator
from pathlib import Path
from typing import Any

import httpx
import pytest
import pytest_asyncio
import respx

from app.external.dummyjson import DummyJSONClient

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _load(name: str) -> Any:
    return json.loads((FIXTURES_DIR / f"{name}.json").read_text())


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--live-api",
        action="store_true",
        default=False,
        help="Run against real dummyjson.com (requires internet)",
    )


@pytest.fixture
def live_api(request: pytest.FixtureRequest) -> bool:
    return bool(request.config.getoption("--live-api"))


@pytest_asyncio.fixture
async def dummyjson(live_api: bool) -> AsyncGenerator[DummyJSONClient, None]:
    if live_api:
        async with DummyJSONClient() as client:
            yield client
        return

    users_data = _load("users")
    products_data = _load("products")
    posts_data = _load("posts")

    user1 = users_data["users"][0]
    product1 = products_data["products"][0]
    post1 = posts_data["posts"][0]

    with respx.mock(base_url="https://dummyjson.com", assert_all_called=False) as mock:
        # ── Users ──────────────────────────────────────────────────────────
        mock.get("/users").mock(return_value=httpx.Response(200, json=users_data))
        mock.get("/users/1").mock(return_value=httpx.Response(200, json=user1))
        mock.get("/users/999").mock(
            return_value=httpx.Response(404, json={"message": "User with id '999' not found"})
        )
        # Wildcard для любого другого числового user_id
        mock.get(url__regex=r"/users/\d+$").mock(return_value=httpx.Response(200, json=user1))
        mock.get(url__regex=r"/users/search").mock(
            return_value=httpx.Response(
                200,
                json={"users": [user1], "total": 1, "skip": 0, "limit": 10},
            )
        )
        mock.post("/users/add").mock(return_value=httpx.Response(201, json={**user1, "id": 101}))
        mock.put("/users/1").mock(
            return_value=httpx.Response(200, json={**user1, "firstName": "Updated"})
        )
        mock.delete("/users/1").mock(
            return_value=httpx.Response(
                200, json={**user1, "isDeleted": True, "deletedOn": "2026-01-01"}
            )
        )

        # ── Products ────────────────────────────────────────────────────────
        mock.get("/products").mock(return_value=httpx.Response(200, json=products_data))
        mock.get("/products/1").mock(return_value=httpx.Response(200, json=product1))
        mock.get(url__regex=r"/products/category/").mock(
            return_value=httpx.Response(
                200,
                json={"products": [product1], "total": 1, "skip": 0, "limit": 10},
            )
        )
        mock.get(url__regex=r"/products/search").mock(
            return_value=httpx.Response(
                200,
                json={"products": [product1], "total": 1, "skip": 0, "limit": 10},
            )
        )

        # ── Posts ───────────────────────────────────────────────────────────
        mock.get("/posts").mock(return_value=httpx.Response(200, json=posts_data))
        mock.get("/posts/1").mock(return_value=httpx.Response(200, json=post1))
        mock.get(url__regex=r"/posts/user/").mock(
            return_value=httpx.Response(
                200,
                json={"posts": [post1], "total": 1, "skip": 0, "limit": 10},
            )
        )

        # ── Auth ────────────────────────────────────────────────────────────
        def auth_handler(request: httpx.Request) -> httpx.Response:
            body = json.loads(request.content)
            if body.get("username") == "emilys":
                return httpx.Response(
                    200,
                    json={
                        "id": 1,
                        "username": "emilys",
                        "email": "emily.johnson@x.dummyjson.com",
                        "firstName": "Emily",
                        "lastName": "Johnson",
                        "gender": "female",
                        "image": "https://dummyjson.com/icon/emilys/128",
                        "accessToken": (
                            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
                            "eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMifQ.test"
                        ),
                        "refreshToken": (
                            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.refresh"
                        ),
                    },
                )
            return httpx.Response(400, json={"message": "Invalid credentials"})

        mock.post("/auth/login").mock(side_effect=auth_handler)

        async with DummyJSONClient() as client:
            yield client
