"""Base Page Object с AI assertions через Claude API."""
from __future__ import annotations
import os
from playwright.async_api import Page, Locator, expect


class BasePage:
    URL: str = ""

    def __init__(self, page: Page) -> None:
        self.page = page

    async def navigate(self) -> None:
        await self.page.goto(self.URL)
        await self.page.wait_for_load_state("networkidle")

    async def ai_assert(self, locator: Locator, expectation: str) -> None:
        """Семантическая проверка через Claude API. Fallback на visible."""
        try:
            import anthropic
            text = await locator.inner_text()
            client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
            msg = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=64,
                messages=[{"role": "user", "content":
                    f"Text: '{text}'\nExpectation: '{expectation}'\nReply ONLY: PASS or FAIL: <reason>"}],
            )
            result = msg.content[0].text.strip()
            if result.startswith("FAIL"):
                raise AssertionError(f"AI assertion failed: {result}")
        except AssertionError:
            raise
        except Exception:
            await expect(locator).to_be_visible()
