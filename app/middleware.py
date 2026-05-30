"""
Middleware стек:
- RequestIDMiddleware  — уникальный X-Request-ID на каждый запрос
- LoggingMiddleware    — structured logging каждого запроса
- RateLimitMiddleware  — простой in-memory rate limit (prod: Redis)
"""

from __future__ import annotations

import time
import uuid
from collections import defaultdict
from collections.abc import Callable

import structlog
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

logger = structlog.get_logger(__name__)


class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Добавляет X-Request-ID к каждому запросу/ответу.
    Если клиент передал свой ID — используем его (для distributed tracing).
    """

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())

        # Кладём в structlog context — все логи в рамках запроса получат request_id
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(request_id=request_id)

        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response


class LoggingMiddleware(BaseHTTPMiddleware):
    """Structured logging каждого HTTP запроса с duration."""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
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


class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    Простой sliding window rate limiter — in-memory.
    Production: заменить на Redis-based (sliding window counter).
    Лимит: 100 req/min per IP. Исключения: /health.
    """

    LIMIT = 100
    WINDOW = 60.0
    EXEMPT_PATHS = {"/health", "/docs", "/openapi.json", "/redoc"}

    def __init__(self, app: ASGIApp, limit: int = 100, window: float = 60.0) -> None:
        super().__init__(app)
        self.limit = limit
        self.window = window
        self._requests: dict[str, list[float]] = defaultdict(list)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if request.url.path in self.EXEMPT_PATHS:
            return await call_next(request)

        client_ip = request.client.host if request.client else "unknown"
        now = time.time()

        # Удаляем старые записи за пределами окна
        window_start = now - self.window
        self._requests[client_ip] = [t for t in self._requests[client_ip] if t > window_start]

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
        return await call_next(request)
