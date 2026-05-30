"""Тесты frontend routes — /login, /dashboard."""

from __future__ import annotations

import pytest
from httpx import AsyncClient


@pytest.mark.api
class TestFrontendRoutes:
    async def test_login_page_serves_html(self, client: AsyncClient) -> None:
        """main.py:83-84 — /login route."""
        resp = await client.get("/login")
        assert resp.status_code == 200
        assert "text/html" in resp.headers.get("content-type", "")

    async def test_dashboard_page_serves_html(self, client: AsyncClient) -> None:
        """main.py:87-88 — /dashboard route."""
        resp = await client.get("/dashboard")
        assert resp.status_code == 200
        assert "text/html" in resp.headers.get("content-type", "")

    async def test_login_page_contains_form(self, client: AsyncClient) -> None:
        resp = await client.get("/login")
        assert b"QA Sentinel" in resp.content

    async def test_dashboard_has_logout_element(self, client: AsyncClient) -> None:
        resp = await client.get("/dashboard")
        assert b"logout" in resp.content.lower()
