"""
E2E тесты auth flow — Playwright против реального фронтенда.
Запуск: make test-e2e (нужен make up)
"""

from __future__ import annotations

import pytest
import pytest_asyncio
from playwright.async_api import Page

from tests.e2e.pages.dashboard_page import DashboardPage
from tests.e2e.pages.login_page import LoginPage


@pytest_asyncio.fixture
async def login_page(page: Page, base_url: str) -> LoginPage:
    lp = LoginPage(page)
    await page.goto(f"{base_url}/login")
    await page.wait_for_load_state("networkidle")
    return lp


@pytest.mark.e2e
class TestLoginFlow:
    async def test_successful_login_redirects_to_dashboard(self, login_page: LoginPage) -> None:
        await login_page.login("test_user", "test_pass")
        await login_page.expect_redirected_to_dashboard()

    async def test_wrong_password_shows_error(self, login_page: LoginPage) -> None:
        await login_page.login("test_user", "wrong_password_xyz")
        await login_page.expect_error_visible()

    async def test_empty_credentials_shows_error(self, login_page: LoginPage) -> None:
        await login_page.login("", "")
        await login_page.expect_error_visible()

    async def test_sql_injection_safely_rejected(self, login_page: LoginPage) -> None:
        await login_page.login("' OR '1'='1", "' OR '1'='1")
        await login_page.expect_error_visible()

    async def test_xss_in_username_safe(self, login_page: LoginPage) -> None:
        await login_page.login("<script>alert(1)</script>", "pass")
        await login_page.expect_error_visible()

    @pytest.mark.parametrize(
        ("username", "password"),
        [
            ("admin", "wrongpass"),
            ("nonexistent@ghost.com", "somepass"),
            ("a" * 100, "pass"),
        ],
    )
    async def test_invalid_credentials_parametrized(
        self, login_page: LoginPage, username: str, password: str
    ) -> None:
        await login_page.login(username, password)
        await login_page.expect_error_visible()


@pytest.mark.e2e
class TestDashboard:
    async def test_dashboard_shows_welcome_after_login(self, page: Page, base_url: str) -> None:
        lp = LoginPage(page)
        await page.goto(f"{base_url}/login")
        await lp.login("test_user", "test_pass")
        await lp.expect_redirected_to_dashboard()

        dp = DashboardPage(page)
        await dp.expect_authenticated()
        await dp.expect_welcome_contains("test_user")

    async def test_logout_returns_to_login(self, page: Page, base_url: str) -> None:
        lp = LoginPage(page)
        await page.goto(f"{base_url}/login")
        await lp.login("test_user", "test_pass")
        await lp.expect_redirected_to_dashboard()

        dp = DashboardPage(page)
        await dp.logout()
        await lp.expect_on_login_page()

    async def test_direct_dashboard_access_without_auth(self, page: Page, base_url: str) -> None:
        """
        Открываем /dashboard без логина.
        Фронтенд проверяет sessionStorage — нет токена → остаёмся на dashboard
        но без данных пользователя (SPA, нет server-side redirect).
        Logout button не должен показываться без сессии.
        """
        await page.goto(f"{base_url}/dashboard")
        await page.wait_for_load_state("networkidle")
        # Страница загрузилась — фронтенд рендерит login view если нет сессии
        # Проверяем что submit button виден (login form)
        submit = page.get_by_test_id("submit-btn")
        await submit.wait_for(state="visible", timeout=3000)


@pytest.mark.e2e
class TestLoginPageUI:
    async def test_login_form_elements_present(self, login_page: LoginPage) -> None:
        assert await login_page.username_input.is_visible()
        assert await login_page.password_input.is_visible()
        assert await login_page.submit_btn.is_visible()

    async def test_submit_button_text(self, login_page: LoginPage) -> None:
        text = await login_page.submit_btn.text_content()
        assert text is not None
        assert "sign in" in text.lower()

    async def test_password_field_is_masked(self, login_page: LoginPage) -> None:
        input_type = await login_page.password_input.get_attribute("type")
        assert input_type == "password"

    async def test_error_hidden_initially(self, login_page: LoginPage) -> None:
        await login_page.error_msg.wait_for(state="hidden", timeout=1000)
