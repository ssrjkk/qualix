from __future__ import annotations

import os

import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "locale": "ru-RU",
        "timezone_id": "Europe/Moscow",
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("E2E_BASE_URL", "http://localhost:8080")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    slow_mo = int(os.environ.get("E2E_SLOWMO", "0"))
    return {
        **browser_type_launch_args,
        "headless": os.environ.get("E2E_HEADED", "0") != "1",
        "slow_mo": slow_mo,
        "args": ["--no-sandbox", "--disable-dev-shm-usage"],
    }


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            p.chromium.launch(headless=True).close()
    except Exception:
        skip_e2e = pytest.mark.skip(
            reason="Playwright browsers not installed - run 'playwright install chromium'"
        )
        for item in items:
            if "e2e" in item.keywords:
                item.add_marker(skip_e2e)
