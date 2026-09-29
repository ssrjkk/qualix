"""
Prometheus metrics endpoint.
Экспортирует метрики приложения для Prometheus.
"""

from __future__ import annotations

from fastapi import APIRouter, Response

router = APIRouter(tags=["metrics"])

# Prometheus client опционален — если не установлен, возвращаем пустой response
try:
    from prometheus_client import (
        CONTENT_TYPE_LATEST,
        Counter,
        Gauge,
        Histogram,
        generate_latest,
    )

    # HTTP request metrics
    http_requests_total = Counter(
        "http_requests_total",
        "Total HTTP requests",
        ["method", "endpoint", "status"],
    )

    http_request_duration_seconds = Histogram(
        "http_request_duration_seconds",
        "HTTP request duration in seconds",
        ["method", "endpoint"],
        buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0),
    )

    # Application metrics
    app_info = Gauge(
        "app_info",
        "Application information",
        ["version", "environment"],
    )

    active_connections = Gauge(
        "active_connections",
        "Number of active database connections",
    )

    METRICS_AVAILABLE = True

except ImportError:  # pragma: no cover
    METRICS_AVAILABLE = False


@router.get("/metrics", include_in_schema=False)
async def metrics() -> Response:
    """
    Prometheus metrics endpoint.
    Возвращает метрики в формате Prometheus exposition format.
    """
    if not METRICS_AVAILABLE:
        return Response(
            content="# Prometheus client not installed\n",
            media_type="text/plain",
        )

    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
