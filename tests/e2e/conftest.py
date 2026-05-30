"""
E2E layer conftest — Playwright fixtures.
pytest-playwright предоставляет browser/context/page автоматически.
Здесь — кастомизация: base_url, viewport, timeouts, трейсинг.
"""

from __future__ import annotations

import os
from collections.abc import Generator

import pytest
from playwright.sync_api import Browser, BrowserContext, Page

# ── Playwright настройки ──────────────────────────────────────────────────────


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    """Расширяем дефолтные context args: viewport, locale, timezone."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "locale": "ru-RU",
        "timezone_id": "Europe/Moscow",
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session")
def base_url() -> str:
    """URL тестируемого приложения — берём из env или дефолт."""
    return os.environ.get("E2E_BASE_URL", "http://localhost:8080")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    """Headless по умолчанию, slowMo для отладки через E2E_SLOWMO=200."""
    slow_mo = int(os.environ.get("E2E_SLOWMO", "0"))
    return {
        **browser_type_launch_args,
        "headless": os.environ.get("E2E_HEADED", "0") != "1",
        "slow_mo": slow_mo,
        "args": ["--no-sandbox", "--disable-dev-shm-usage"],
    }


@pytest.fixture
def context(browser: Browser, browser_context_args: dict) -> Generator[BrowserContext, None, None]:
    """
    Каждый тест — свежий browser context (изолированные cookies/storage).
    Трейсинг включён — при падении сохраняем trace.zip.
    """
    ctx = browser.new_context(**browser_context_args)
    ctx.set_default_timeout(10_000)  # 10s на любое действие
    ctx.set_default_navigation_timeout(20_000)

    # Playwright tracing — включаем если E2E_TRACE=1
    if os.environ.get("E2E_TRACE", "0") == "1":
        ctx.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield ctx

    if os.environ.get("E2E_TRACE", "0") == "1":
        trace_dir = "allure-results/traces"
        os.makedirs(trace_dir, exist_ok=True)
        ctx.tracing.stop(path=f"{trace_dir}/trace.zip")

    ctx.close()


@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Page с авто-скриншотом при падении теста."""
    page = context.new_page()

    yield page

    # Screenshot on failure
    if hasattr(page, "_test_failed") and page._test_failed:  # type: ignore[attr-defined]
        import allure  # type: ignore[import-untyped]

        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot, name="screenshot_on_failure", attachment_type=allure.attachment_type.PNG
        )

    page.close()


@pytest.fixture
def logged_in_page(page: Page, base_url: str) -> Page:
    """Page с уже выполненным логином — переиспользуй в тестах после авторизации."""
    page.goto(f"{base_url}/login")
    page.get_by_label("Username").fill("test_user")
    page.get_by_label("Password").fill("test_pass")
    page.get_by_role("button", name="Sign in").click()
    page.wait_for_url("**/dashboard")
    return page


# ── Маркеры для запуска/пропуска ─────────────────────────────────────────────


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """
    Если нет доступного браузера (CI без playwright install) —
    пропускаем e2e тесты с информативным сообщением.
    """
    skip_e2e = pytest.mark.skip(
        reason="Playwright browsers not installed — run 'playwright install chromium'"
    )
    for item in items:
        if "e2e" in item.keywords:
            try:
                from playwright.sync_api import sync_playwright

                with sync_playwright() as p:
                    p.chromium.launch(headless=True).close()
            except Exception:
                item.add_marker(skip_e2e)
                break
