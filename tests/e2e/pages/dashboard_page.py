"""Dashboard Page Object"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from tests.e2e.pages.base_page import BasePage


class DashboardPage(BasePage):
    URL = "/dashboard"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.logout_btn = page.get_by_test_id("logout-btn")
        self.welcome_text = page.locator(".welcome")

    def logout(self) -> None:
        self.logout_btn.click()

    def expect_welcome_contains(self, username: str) -> None:
        expect(self.welcome_text).to_contain_text(username)

    def expect_authenticated(self) -> None:
        expect(self.logout_btn).to_be_visible()
