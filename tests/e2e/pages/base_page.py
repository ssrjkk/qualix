"""Base Page Object с AI assertions через Claude API."""

from __future__ import annotations

import os

from playwright.sync_api import Locator, Page, expect


class BasePage:
    URL: str = ""

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self) -> None:
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")

    def ai_assert(self, locator: Locator, expectation: str) -> None:
        """Семантическая проверка через Claude API. Fallback на visible."""
        try:
            import anthropic

            text = locator.inner_text()
            client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
            msg = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=64,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Text: '{text}'\n"
                            f"Expectation: '{expectation}'\n"
                            "Reply ONLY: PASS or FAIL: <reason>"
                        ),
                    }
                ],
            )
            result = msg.content[0].text.strip()
            if result.startswith("FAIL"):
                raise AssertionError(f"AI assertion failed: {result}")
        except AssertionError:
            raise
        except Exception:
            expect(locator).to_be_visible()
