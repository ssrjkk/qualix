"""
Middleware стек:
- RequestIDMiddleware  — уникальный X-Request-ID на каждый запрос
- LoggingMiddleware    — structured logging каждого запроса
- RateLimitMiddleware  — простой in-memory rate limit (prod: Redis)
"""

from __future__ import annotations

import re
import time
import uuid
from collections.abc import Awaitable, Callable

import structlog
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

logger = structlog.get_logger(__name__)

_REQUEST_ID_RE = re.compile(r"^[a-zA-Z0-9\-_]{1,64}$")


class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Добавляет X-Request-ID к каждому запросу/ответу.
    Клиентский ID валидируется; если невалиден — генерируем server-side.
    """

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        client_id = request.headers.get("X-Request-ID", "")
        request_id = client_id if _REQUEST_ID_RE.match(client_id) else str(uuid.uuid4())

        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(request_id=request_id)

        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response


class LoggingMiddleware(BaseHTTPMiddleware):
    """Structured logging каждого HTTP запроса с duration."""

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        start = time.perf_counter()
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - start) * 1000, 2)

        logger.info(
            "http_request",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=duration_ms,
            client=request.client.host if request.client else "unknown",
        )
        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add security headers to every response."""

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        response.headers["X-XSS-Protection"] = "0"
        return response


class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    Sliding window rate limiter — in-memory.
    Production: заменить на Redis-based (sliding window counter).
    Лимит: 100 req/min per IP. Исключения: /health.
    """

    LIMIT = 100
    WINDOW = 60.0
    EXEMPT_PATHS = {"/health", "/docs", "/openapi.json", "/redoc"}
    _MAX_ENTRIES = 10_000
    _CLEANUP_INTERVAL = 100

    def __init__(self, app: ASGIApp, limit: int = 100, window: float = 60.0) -> None:
        super().__init__(app)
        self.limit = limit
        self.window = window
        self._requests: dict[str, list[float]] = {}
        self._request_count = 0

    def _cleanup_stale(self, now: float) -> None:
        cutoff = now - self.window
        stale_keys = [k for k, v in self._requests.items() if not v or v[-1] <= cutoff]
        for k in stale_keys:
            del self._requests[k]

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        if request.url.path in self.EXEMPT_PATHS:
            return await call_next(request)

        client_ip = request.client.host if request.client else "unknown"
        now = time.monotonic()

        self._request_count += 1
        if self._request_count % self._CLEANUP_INTERVAL == 0:
            self._cleanup_stale(now)
            if len(self._requests) > self._MAX_ENTRIES:
                self._cleanup_stale(now)

        window_start = now - self.window
        if client_ip in self._requests:
            self._requests[client_ip] = [t for t in self._requests[client_ip] if t > window_start]
        else:
            self._requests[client_ip] = []

        if len(self._requests[client_ip]) >= self.limit:
            logger.warning(
                "rate_limit_exceeded",
                client_ip=client_ip,
                path=request.url.path,
                requests_in_window=len(self._requests[client_ip]),
            )
            return Response(
                content='{"detail":"Too many requests"}',
                status_code=429,
                headers={
                    "Content-Type": "application/json",
                    "Retry-After": str(int(self.window)),
                    "X-RateLimit-Limit": str(self.limit),
                    "X-RateLimit-Reset": str(int(now + self.window)),
                },
            )

        self._requests[client_ip].append(now)
        response = await call_next(request)
        remaining = max(0, self.limit - len(self._requests[client_ip]))
        response.headers["X-RateLimit-Limit"] = str(self.limit)
        response.headers["X-RateLimit-Remaining"] = str(remaining)
        response.headers["X-RateLimit-Reset"] = str(int(now + self.window))
        return response
