"""Semantic assertions exercised through real HTTP against a loopback fake API."""

from __future__ import annotations

import json
import threading
from collections.abc import Iterator
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, cast
from unittest.mock import Mock

import pytest
from playwright.sync_api import Locator, Page

from tests.e2e.pages import base_page
from tests.e2e.pages.base_page import AIProviderError, BasePage, _AIConfig

pytestmark = pytest.mark.unit


@dataclass
class FakeAPI:
    url: str = ""
    status: int = 200
    body: Any = None
    disconnect: bool = False
    stall: bool = False
    requests: list[tuple[str, dict[str, str], Any]] = field(default_factory=list)


@pytest.fixture(autouse=True)
def clean_ai_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for prefix in ("AI", "ANTHROPIC", "OPENAI"):
        for suffix in ("PROVIDER", "BASE_URL", "API_KEY", "MODEL"):
            monkeypatch.delenv(f"{prefix}_{suffix}", raising=False)
    # Local HTTP must not go through a developer's corporate proxy.
    monkeypatch.setenv("NO_PROXY", "127.0.0.1,localhost")


@pytest.fixture
def fake_api(monkeypatch: pytest.MonkeyPatch) -> Iterator[FakeAPI]:
    api = FakeAPI()
    release = threading.Event()

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            headers = {key.lower(): value for key, value in self.headers.items()}
            api.requests.append((self.path, headers, body))
            if api.stall:
                release.wait(5)
                return
            if api.disconnect:
                self.close_connection = True
                return
            content = api.body if isinstance(api.body, bytes) else json.dumps(api.body).encode()
            self.send_response(api.status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

        def log_message(self, format: str, *args: Any) -> None:
            pass

    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        api.url = f"http://127.0.0.1:{server.server_port}"
        monkeypatch.setenv("AI_BASE_URL", api.url + "/v1/")
        monkeypatch.setenv("AI_API_KEY", "local-test-key")
        monkeypatch.setenv("AI_MODEL", "local-test-model")
        thread = threading.Thread(target=server.serve_forever, kwargs={"poll_interval": 0.01})
        thread.start()
        try:
            yield api
        finally:
            release.set()
            server.shutdown()
            thread.join(timeout=5)


@pytest.fixture
def page_object() -> BasePage:
    return BasePage(cast(Page, Mock(spec=Page)))


@pytest.fixture
def locator() -> Mock:
    result = Mock(spec=Locator)
    result.inner_text.return_value = "Payment completed"
    return result


def response(provider: str, text: Any = "PASS") -> dict[str, Any]:
    if provider == "anthropic":
        return {
            "type": "message",
            "role": "assistant",
            "stop_reason": "end_turn",
            "content": [{"type": "text", "text": text}],
        }
    return {
        "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": text}}]
    }


@pytest.mark.parametrize("provider", ["anthropic", "openai", "openai-compatible"])
def test_exact_pass_uses_real_provider_http(
    provider: str,
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    fake_api.body = response(provider)
    page_object.ai_assert(locator, "The payment succeeded")
    assert len(fake_api.requests) == 1
    path, headers, payload = fake_api.requests[0]
    assert payload["model"] == "local-test-model"
    assert payload["max_tokens"] == 64
    assert json.loads(payload["messages"][-1]["content"]) == {
        "text": "Payment completed",
        "expectation": "The payment succeeded",
    }
    if provider == "anthropic":
        assert path == "/v1/messages"
        assert headers["x-api-key"] == "local-test-key"
        assert headers["anthropic-version"] == "2023-06-01"
        assert "authorization" not in headers
        assert "exactly PASS" in payload["system"]
    else:
        assert path == "/v1/chat/completions"
        assert headers["authorization"] == "Bearer local-test-key"
        assert "x-api-key" not in headers
        assert payload["messages"][0]["role"] == "system"


@pytest.mark.parametrize("provider", ["anthropic", "openai"])
@pytest.mark.parametrize(
    "text",
    ["FAIL: wrong content", "", "pass", "PASS: yes", " PASS", "PASS\n", "Maybe", "PASS\nFAIL"],
)
def test_only_exact_pass_succeeds(
    provider: str,
    text: str,
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    fake_api.body = response(provider, text)
    with pytest.raises(AssertionError, match="requires exact PASS"):
        page_object.ai_assert(locator, "The payment succeeded")


@pytest.mark.parametrize("provider", ["anthropic", "openai"])
@pytest.mark.parametrize("body", [None, [], {}, {"error": "bad request"}, b"not json"])
def test_malformed_response_is_provider_error(
    provider: str,
    body: Any,
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    fake_api.body = body
    with pytest.raises(AIProviderError, match="invalid"):
        page_object.ai_assert(locator, "The payment succeeded")


@pytest.mark.parametrize("provider", ["anthropic", "openai"])
@pytest.mark.parametrize("kind", ["truncated", "multiple", "empty", "tool", "nontext", "refusal"])
def test_incomplete_or_nontext_generation_cannot_pass(
    provider: str,
    kind: str,
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    data = response(provider)
    if provider == "anthropic":
        if kind == "truncated":
            data["stop_reason"] = "max_tokens"
        elif kind == "multiple":
            data["content"] *= 2
        elif kind == "empty":
            data["content"] = []
        elif kind == "tool":
            data["content"][0]["type"] = "tool_use"
        elif kind == "refusal":
            data["stop_reason"] = "refusal"
        else:
            data["content"][0]["text"] = None
    else:
        if kind == "truncated":
            data["choices"][0]["finish_reason"] = "length"
        elif kind == "multiple":
            data["choices"] *= 2
        elif kind == "empty":
            data["choices"] = []
        elif kind == "tool":
            data["choices"][0]["message"]["tool_calls"] = [{"type": "function"}]
        elif kind == "refusal":
            data["choices"][0]["message"]["refusal"] = "Cannot comply"
        else:
            data["choices"][0]["message"]["content"] = None
    fake_api.body = data
    with pytest.raises(AIProviderError, match="invalid or incomplete"):
        page_object.ai_assert(locator, "The payment succeeded")


@pytest.mark.parametrize("provider", ["anthropic", "openai"])
@pytest.mark.parametrize("status", [302, 401, 429, 500])
def test_http_errors_are_not_semantic_passes(
    provider: str,
    status: int,
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    fake_api.status = status
    fake_api.body = response(provider)
    with pytest.raises(AIProviderError, match=f"HTTP {status}") as error:
        page_object.ai_assert(locator, "The payment succeeded")
    assert "local-test-key" not in str(error.value)
    assert len(fake_api.requests) == 1


@pytest.mark.parametrize("provider", ["anthropic", "openai"])
@pytest.mark.parametrize("kind", ["disconnect", "timeout"])
def test_transport_errors_are_not_semantic_passes(
    provider: str,
    kind: str,
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    fake_api.disconnect = kind == "disconnect"
    fake_api.stall = kind == "timeout"
    monkeypatch.setattr(base_page, "AI_TIMEOUT_SECONDS", 0.2)
    with pytest.raises(AIProviderError, match="transport error"):
        page_object.ai_assert(locator, "The payment succeeded")


@pytest.mark.parametrize("provider", ["anthropic", "openai"])
def test_missing_credentials_fail_without_visibility_fallback(
    provider: str,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    visible = Mock()
    monkeypatch.setattr(base_page, "expect", visible)
    with pytest.raises(AIProviderError, match="API_KEY"):
        page_object.ai_assert(locator, "The payment succeeded")
    visible.assert_not_called()
    locator.inner_text.assert_not_called()


def test_legacy_anthropic_config(
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    for name in ("AI_API_KEY", "AI_MODEL", "AI_BASE_URL"):
        monkeypatch.setenv(name, "")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "legacy-key")
    monkeypatch.setenv("ANTHROPIC_BASE_URL", fake_api.url)
    fake_api.body = response("anthropic")
    page_object.ai_assert(locator, "The payment succeeded")
    path, headers, payload = fake_api.requests[0]
    assert path == "/v1/messages"
    assert headers["x-api-key"] == "legacy-key"
    assert payload["model"] == "claude-sonnet-4-20250514"


def test_generic_config_overrides_provider_env(
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "unused-key")
    monkeypatch.setenv("ANTHROPIC_MODEL", "unused-model")
    monkeypatch.setenv("ANTHROPIC_BASE_URL", "https://invalid.example")
    monkeypatch.setenv("AI_BASE_URL", fake_api.url + "/proxy/v1")
    fake_api.body = response("anthropic")
    page_object.ai_assert(locator, "The payment succeeded")
    assert fake_api.requests[0][0] == "/proxy/v1/messages"
    assert fake_api.requests[0][1]["x-api-key"] == "local-test-key"
    assert fake_api.requests[0][2]["model"] == "local-test-model"


@pytest.mark.parametrize("provider", ["anthropic", "openai"])
def test_provider_specific_model_and_defaults(
    provider: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("AI_PROVIDER", provider)
    monkeypatch.setenv(f"{provider.upper()}_API_KEY", "provider-key")
    monkeypatch.setenv(f"{provider.upper()}_MODEL", "provider-model")
    config = _AIConfig.from_env()
    assert config.base_url == f"https://api.{provider}.com/v1"
    assert config.model == "provider-model"
    assert config.api_key == "provider-key"
    assert "provider-key" not in repr(config)


@pytest.mark.parametrize(
    ("name", "value", "error"),
    [
        ("AI_PROVIDER", "unknown", "AI_PROVIDER"),
        ("AI_MODEL", "", "AI_MODEL"),
        ("AI_API_KEY", " ", "API_KEY"),
        ("AI_BASE_URL", "file:///tmp/api", "AI_BASE_URL"),
        ("AI_BASE_URL", "https://user:secret@example.com/v1", "AI_BASE_URL"),
        ("AI_BASE_URL", "https://example.com/v1?key=secret", "AI_BASE_URL"),
        ("AI_BASE_URL", "https://example.com/v1#fragment", "AI_BASE_URL"),
        ("AI_BASE_URL", "https://[invalid", "AI_BASE_URL"),
    ],
)
def test_invalid_config_fails_before_http(
    name: str,
    value: str,
    error: str,
    fake_api: FakeAPI,
    monkeypatch: pytest.MonkeyPatch,
    page_object: BasePage,
    locator: Mock,
) -> None:
    monkeypatch.setenv("AI_PROVIDER", "openai")
    monkeypatch.setenv(name, value)
    with pytest.raises(AIProviderError, match=error):
        page_object.ai_assert(locator, "The payment succeeded")
    assert not fake_api.requests


def test_locator_only_assertion_is_separate(
    monkeypatch: pytest.MonkeyPatch, page_object: BasePage, locator: Mock
) -> None:
    visible = Mock()
    monkeypatch.setattr(base_page, "expect", visible)
    page_object.assert_visible(locator)
    visible.assert_called_once_with(locator)
    visible.return_value.to_be_visible.assert_called_once_with()


def test_locator_errors_are_not_swallowed(
    fake_api: FakeAPI, page_object: BasePage, locator: Mock
) -> None:
    locator.inner_text.side_effect = RuntimeError("detached locator")
    with pytest.raises(RuntimeError, match="detached locator"):
        page_object.ai_assert(locator, "The payment succeeded")
    assert not fake_api.requests
