"""Unit тесты middleware — RequestID, Logging, RateLimit."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest


def _make_request(
    path: str = "/api/v1/users",
    method: str = "GET",
    client_ip: str = "127.0.0.1",
    headers: dict | None = None,
) -> MagicMock:
    req = MagicMock()
    req.url.path = path
    req.method = method
    req.client = MagicMock()
    req.client.host = client_ip
    req.headers = MagicMock()
    req.headers.get = MagicMock(return_value=headers.get("X-Request-ID") if headers else None)
    return req


def _make_response(status_code: int = 200) -> MagicMock:
    resp = MagicMock()
    resp.status_code = status_code
    resp.headers = {}
    return resp


@pytest.mark.unit
class TestRequestIDMiddleware:
    async def test_adds_request_id_to_response(self) -> None:
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import RequestIDMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(RequestIDMiddleware)

        with TestClient(app) as client:
            resp = client.get("/test")
        assert "x-request-id" in resp.headers

    async def test_uses_client_request_id_if_provided(self) -> None:
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import RequestIDMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(RequestIDMiddleware)

        custom_id = "my-custom-request-id-123"
        with TestClient(app) as client:
            resp = client.get("/test", headers={"X-Request-ID": custom_id})
        assert resp.headers["x-request-id"] == custom_id

    async def test_generates_uuid_if_no_request_id(self) -> None:
        import re

        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import RequestIDMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(RequestIDMiddleware)

        with TestClient(app) as client:
            resp = client.get("/test")

        rid = resp.headers["x-request-id"]
        # UUID4 format
        assert re.match(r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", rid)


@pytest.mark.unit
class TestSecurityHeadersMiddleware:
    async def test_adds_security_headers(self) -> None:
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import SecurityHeadersMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(SecurityHeadersMiddleware)

        with TestClient(app) as client:
            resp = client.get("/test")

        assert resp.headers["x-content-type-options"] == "nosniff"
        assert resp.headers["x-frame-options"] == "DENY"
        assert resp.headers["referrer-policy"] == "strict-origin-when-cross-origin"
        assert resp.headers["permissions-policy"] == "camera=(), microphone=(), geolocation=()"
        assert resp.headers["x-xss-protection"] == "0"


@pytest.mark.unit
class TestRateLimitMiddleware:
    async def test_allows_requests_under_limit(self) -> None:
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import RateLimitMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(RateLimitMiddleware, limit=10, window=60.0)

        with TestClient(app) as client:
            for _ in range(5):
                resp = client.get("/test")
                assert resp.status_code == 200

    async def test_blocks_requests_over_limit(self) -> None:
        """превышение лимита → 429."""
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import RateLimitMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(RateLimitMiddleware, limit=3, window=60.0)

        with TestClient(app) as client:
            for _ in range(3):
                client.get("/test")
            # 4й запрос должен быть заблокирован
            resp = client.get("/test")
            assert resp.status_code == 429
            assert resp.json()["detail"] == "Too many requests"

    async def test_health_endpoint_exempt_from_rate_limit(self) -> None:
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import RateLimitMiddleware

        app = FastAPI()

        @app.get("/health")
        async def health() -> dict:
            return {"status": "ok"}

        app.add_middleware(RateLimitMiddleware, limit=1, window=60.0)

        with TestClient(app) as client:
            # /health исключён — не считается в лимит
            for _ in range(5):
                resp = client.get("/health")
                assert resp.status_code == 200

    async def test_rate_limit_response_has_headers(self) -> None:
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import RateLimitMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(RateLimitMiddleware, limit=1, window=60.0)

        with TestClient(app) as client:
            client.get("/test")
            resp = client.get("/test")

        assert resp.status_code == 429
        assert "x-ratelimit-limit" in resp.headers
        assert "retry-after" in resp.headers


@pytest.mark.unit
class TestRateLimitMemoryGuard:
    """Ограничение памяти словаря с таймстампами — иначе лимитер течь при смене IP."""

    def test_cleanup_stale_drops_expired_and_empty_keys(self) -> None:
        from app.middleware import RateLimitMiddleware

        mw = RateLimitMiddleware(app=MagicMock(), limit=100, window=60.0)
        now = 1000.0
        mw._requests = {
            "fresh": [now],
            "expired": [now - mw.window - 1],
            "empty": [],
        }

        mw._cleanup_stale(now)

        assert list(mw._requests) == ["fresh"]

    async def test_dispatch_prunes_on_cleanup_interval(self, monkeypatch: pytest.MonkeyPatch) -> None:
        from unittest.mock import AsyncMock

        from app.middleware import RateLimitMiddleware

        monkeypatch.setattr("app.middleware.time.monotonic", lambda: 1000.0)

        mw = RateLimitMiddleware(app=MagicMock(), limit=100, window=60.0)
        mw._requests = {f"10.0.{i}.1": [0.0] for i in range(200)}
        mw._request_count = RateLimitMiddleware._CLEANUP_INTERVAL - 1

        call_next = AsyncMock(return_value=_make_response(200))
        await mw.dispatch(_make_request(path="/api/v1/users"), call_next)

        assert list(mw._requests) == ["127.0.0.1"]
        assert call_next.await_count == 1

    async def test_dispatch_runs_second_cleanup_when_over_capacity(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        from unittest.mock import AsyncMock

        from app.middleware import RateLimitMiddleware

        now = 1000.0
        monkeypatch.setattr("app.middleware.time.monotonic", lambda: now)

        mw = RateLimitMiddleware(app=MagicMock(), limit=100, window=60.0)
        mw._requests = {
            f"10.0.{i // 256}.{i % 256}": [now] for i in range(RateLimitMiddleware._MAX_ENTRIES + 1)
        }
        mw._request_count = RateLimitMiddleware._CLEANUP_INTERVAL - 1

        cleanups: list[float] = []
        prune_stale = mw._cleanup_stale

        def counting_prune(ts: float) -> None:
            cleanups.append(ts)
            prune_stale(ts)

        mw._cleanup_stale = counting_prune

        call_next = AsyncMock(return_value=_make_response(200))
        await mw.dispatch(_make_request(path="/api/v1/users"), call_next)

        # записи свежие, поэтому второй проход ничего не удаляет
        assert len(cleanups) == 2
        assert len(mw._requests) == RateLimitMiddleware._MAX_ENTRIES + 2
        assert call_next.await_count == 1


@pytest.mark.unit
class TestLoggingMiddleware:
    async def test_logs_request_info(self) -> None:
        from fastapi import FastAPI
        from starlette.testclient import TestClient

        from app.middleware import LoggingMiddleware

        app = FastAPI()

        @app.get("/test")
        async def test_route() -> dict:
            return {"ok": True}

        app.add_middleware(LoggingMiddleware)

        with TestClient(app) as client:
            resp = client.get("/test")
        assert resp.status_code == 200
