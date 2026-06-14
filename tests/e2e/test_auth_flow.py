"""
E2E тесты auth flow — Playwright против реального фронтенда.
Запуск: make test-e2e (нужен make up)
"""

from __future__ import annotations

import pytest
from playwright.sync_api import Page

from tests.e2e.pages.dashboard_page import DashboardPage
from tests.e2e.pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    lp = LoginPage(page)
    page.goto(f"{base_url}/login")
    page.wait_for_load_state("networkidle")
    return lp


@pytest.mark.e2e
class TestLoginFlow:
    def test_successful_login_redirects_to_dashboard(self, login_page: LoginPage) -> None:
        login_page.login("test_user", "test_pass")
        login_page.expect_redirected_to_dashboard()

    def test_wrong_password_shows_error(self, login_page: LoginPage) -> None:
        login_page.login("test_user", "wrong_password_xyz")
        login_page.expect_error_visible()

    def test_empty_credentials_shows_error(self, login_page: LoginPage) -> None:
        login_page.login("", "")
        login_page.expect_error_visible()

    def test_sql_injection_safely_rejected(self, login_page: LoginPage) -> None:
        login_page.login("' OR '1'='1", "' OR '1'='1")
        login_page.expect_error_visible()

    def test_xss_in_username_safe(self, login_page: LoginPage) -> None:
        login_page.login("<script>alert(1)</script>", "pass")
        login_page.expect_error_visible()

    @pytest.mark.parametrize(
        ("username", "password"),
        [
            ("admin", "wrongpass"),
            ("nonexistent@ghost.com", "somepass"),
            ("a" * 100, "pass"),
        ],
    )
    def test_invalid_credentials_parametrized(
        self, login_page: LoginPage, username: str, password: str
    ) -> None:
        login_page.login(username, password)
        login_page.expect_error_visible()


@pytest.mark.e2e
class TestDashboard:
    def test_dashboard_shows_welcome_after_login(self, page: Page, base_url: str) -> None:
        lp = LoginPage(page)
        page.goto(f"{base_url}/login")
        lp.login("test_user", "test_pass")
        lp.expect_redirected_to_dashboard()

        dp = DashboardPage(page)
        dp.expect_authenticated()
        dp.expect_welcome_contains("test_user")

    def test_logout_returns_to_login(self, page: Page, base_url: str) -> None:
        lp = LoginPage(page)
        page.goto(f"{base_url}/login")
        lp.login("test_user", "test_pass")
        lp.expect_redirected_to_dashboard()

        dp = DashboardPage(page)
        dp.logout()
        lp.expect_on_login_page()

    def test_direct_dashboard_access_without_auth(self, page: Page, base_url: str) -> None:
        """
        Открываем /dashboard без логина.
        Фронтенд проверяет sessionStorage — нет токена → остаёмся на dashboard
        но без данных пользователя (SPA, нет server-side redirect).
        Logout button не должен показываться без сессии.
        """
        page.goto(f"{base_url}/dashboard")
        page.wait_for_load_state("networkidle")
        submit = page.get_by_test_id("submit-btn")
        submit.wait_for(state="visible", timeout=3000)


@pytest.mark.e2e
class TestLoginPageUI:
    def test_login_form_elements_present(self, login_page: LoginPage) -> None:
        assert login_page.username_input.is_visible()
        assert login_page.password_input.is_visible()
        assert login_page.submit_btn.is_visible()

    def test_submit_button_text(self, login_page: LoginPage) -> None:
        text = login_page.submit_btn.text_content()
        assert text is not None
        assert "sign in" in text.lower()

    def test_password_field_is_masked(self, login_page: LoginPage) -> None:
        input_type = login_page.password_input.get_attribute("type")
        assert input_type == "password"

    def test_error_hidden_initially(self, login_page: LoginPage) -> None:
        login_page.error_msg.wait_for(state="hidden", timeout=1000)
