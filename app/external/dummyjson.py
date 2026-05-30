"""
Клиент для dummyjson.com — публичный REST API для тестирования.
Endpoints: /users, /products, /posts, /auth/login

Используется как внешний SUT (System Under Test) в тестах.
В CI тесты запускаются с respx моками — детерминированы без сети.
Для реального прогона против живого API: pytest --live-api
"""

from __future__ import annotations

from typing import Any

import httpx
from pydantic import BaseModel, Field

BASE_URL = "https://dummyjson.com"
TIMEOUT = 10.0


class DummyUser(BaseModel):
    id: int
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    age: int
    gender: str
    username: str
    phone: str

    model_config = {"populate_by_name": True}


class DummyProduct(BaseModel):
    id: int
    title: str
    description: str
    price: float
    discount_percentage: float = Field(alias="discountPercentage")
    rating: float
    stock: int
    category: str

    model_config = {"populate_by_name": True}


class DummyPost(BaseModel):
    id: int
    title: str
    body: str
    user_id: int = Field(alias="userId")
    tags: list[str]
    views: int

    model_config = {"populate_by_name": True}


class PaginatedResponse(BaseModel):
    total: int
    skip: int
    limit: int


class UsersResponse(PaginatedResponse):
    users: list[DummyUser]


class ProductsResponse(PaginatedResponse):
    products: list[DummyProduct]


class PostsResponse(PaginatedResponse):
    posts: list[DummyPost]


class DummyJSONClient:
    """
    Async HTTP клиент для dummyjson.com.
    Передай custom httpx.AsyncClient для тестирования с respx.
    """

    def __init__(self, client: httpx.AsyncClient | None = None) -> None:
        self._client = client or httpx.AsyncClient(
            base_url=BASE_URL,
            timeout=TIMEOUT,
            headers={"Content-Type": "application/json"},
        )

    async def __aenter__(self) -> DummyJSONClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._client.aclose()

    # ── Users ─────────────────────────────────────────────────────────────────

    async def get_users(self, limit: int = 10, skip: int = 0) -> UsersResponse:
        resp = await self._client.get("/users", params={"limit": limit, "skip": skip})
        resp.raise_for_status()
        return UsersResponse.model_validate(resp.json())

    async def get_user(self, user_id: int) -> DummyUser:
        resp = await self._client.get(f"/users/{user_id}")
        resp.raise_for_status()
        return DummyUser.model_validate(resp.json())

    async def search_users(self, query: str) -> UsersResponse:
        resp = await self._client.get("/users/search", params={"q": query})
        resp.raise_for_status()
        return UsersResponse.model_validate(resp.json())

    async def create_user(self, data: dict[str, Any]) -> DummyUser:
        resp = await self._client.post("/users/add", json=data)
        resp.raise_for_status()
        return DummyUser.model_validate(resp.json())

    async def update_user(self, user_id: int, data: dict[str, Any]) -> DummyUser:
        resp = await self._client.put(f"/users/{user_id}", json=data)
        resp.raise_for_status()
        return DummyUser.model_validate(resp.json())

    async def delete_user(self, user_id: int) -> dict[str, Any]:
        resp = await self._client.delete(f"/users/{user_id}")
        resp.raise_for_status()
        return resp.json()  # type: ignore[no-any-return]

    # ── Products ──────────────────────────────────────────────────────────────

    async def get_products(self, limit: int = 10, skip: int = 0) -> ProductsResponse:
        resp = await self._client.get("/products", params={"limit": limit, "skip": skip})
        resp.raise_for_status()
        return ProductsResponse.model_validate(resp.json())

    async def get_product(self, product_id: int) -> DummyProduct:
        resp = await self._client.get(f"/products/{product_id}")
        resp.raise_for_status()
        return DummyProduct.model_validate(resp.json())

    async def get_products_by_category(self, category: str) -> ProductsResponse:
        resp = await self._client.get(f"/products/category/{category}")
        resp.raise_for_status()
        return ProductsResponse.model_validate(resp.json())

    async def search_products(self, query: str) -> ProductsResponse:
        resp = await self._client.get("/products/search", params={"q": query})
        resp.raise_for_status()
        return ProductsResponse.model_validate(resp.json())

    # ── Posts ─────────────────────────────────────────────────────────────────

    async def get_posts(self, limit: int = 10, skip: int = 0) -> PostsResponse:
        resp = await self._client.get("/posts", params={"limit": limit, "skip": skip})
        resp.raise_for_status()
        return PostsResponse.model_validate(resp.json())

    async def get_post(self, post_id: int) -> DummyPost:
        resp = await self._client.get(f"/posts/{post_id}")
        resp.raise_for_status()
        return DummyPost.model_validate(resp.json())

    async def get_user_posts(self, user_id: int) -> PostsResponse:
        resp = await self._client.get(f"/posts/user/{user_id}")
        resp.raise_for_status()
        return PostsResponse.model_validate(resp.json())

    # ── Auth ──────────────────────────────────────────────────────────────────

    async def login(self, username: str, password: str) -> dict[str, Any]:
        resp = await self._client.post(
            "/auth/login",
            json={"username": username, "password": password},
        )
        resp.raise_for_status()
        return resp.json()  # type: ignore[no-any-return]
