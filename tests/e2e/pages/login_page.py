"""Login Page Object — соответствует frontend/index.html"""

from __future__ import annotations

from playwright.async_api import Page, expect

from tests.e2e.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.get_by_test_id("username-input")
        self.password_input = page.get_by_test_id("password-input")
        self.submit_btn = page.get_by_test_id("submit-btn")
        self.error_msg = page.get_by_test_id("auth-error")

    async def login(self, username: str, password: str) -> None:
        await self.username_input.fill(username)
        await self.password_input.fill(password)
        await self.submit_btn.click()

    async def expect_error_visible(self) -> None:
        await expect(self.error_msg).to_be_visible()

    async def expect_redirected_to_dashboard(self) -> None:
        await self.page.wait_for_url("**/dashboard", timeout=5000)

    async def expect_on_login_page(self) -> None:
        await self.page.wait_for_url("**/login", timeout=3000)
