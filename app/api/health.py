"""
Детальный health endpoint — отдельные статусы для каждой зависимости.
/health        — liveness probe (k8s): быстро, без IO
/health/ready  — readiness probe (k8s): проверяет DB + Redis
"""

from __future__ import annotations

import time
from typing import Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import Settings
from app.dependencies import get_db, get_settings
from app.logging_config import get_logger

router = APIRouter(tags=["health"])
logger = get_logger(__name__)


class ComponentStatus(BaseModel):
    status: Literal["ok", "degraded", "down"]
    latency_ms: float | None = None
    detail: str | None = None


class HealthResponse(BaseModel):
    status: Literal["ok", "degraded", "down"]
    version: str
    environment: str
    uptime_s: float
    components: dict[str, ComponentStatus]


_start_time = time.time()


@router.get("/health", response_model=dict)
async def liveness(settings: Settings = Depends(get_settings)) -> dict:
    """
    Liveness probe — k8s убивает pod если этот endpoint недоступен.
    Никакого IO — только проверка что процесс жив.
    """
    return {"status": "ok", "environment": settings.environment}


@router.get("/health/ready", response_model=HealthResponse)
async def readiness(
    db: AsyncSession = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> HealthResponse:
    """
    Readiness probe — k8s не шлёт трафик пока этот endpoint не вернёт ok.
    Проверяет реальные зависимости: DB, Redis.
    """
    components: dict[str, ComponentStatus] = {}
    overall = "ok"

    # ── PostgreSQL / SQLite ───────────────────────────────────────────────────
    t0 = time.perf_counter()
    try:
        await db.execute(text("SELECT 1"))
        db_latency = round((time.perf_counter() - t0) * 1000, 2)
        components["database"] = ComponentStatus(status="ok", latency_ms=db_latency)
    except Exception as e:
        components["database"] = ComponentStatus(status="down", detail=str(e)[:100])
        overall = "down"
        logger.error("health_db_check_failed", error=str(e))

    # ── Redis ─────────────────────────────────────────────────────────────────
    t0 = time.perf_counter()
    try:
        import redis.asyncio as aioredis

        r = aioredis.from_url(settings.redis_url, socket_connect_timeout=1)
        await r.ping()
        await r.aclose()
        redis_latency = round((time.perf_counter() - t0) * 1000, 2)
        components["redis"] = ComponentStatus(status="ok", latency_ms=redis_latency)
    except Exception as e:
        redis_latency = round((time.perf_counter() - t0) * 1000, 2)
        components["redis"] = ComponentStatus(
            status="degraded",
            latency_ms=redis_latency,
            detail="Redis unavailable — running degraded",
        )
        if overall == "ok":
            overall = "degraded"
        logger.warning("health_redis_check_failed", error=str(e))

    return HealthResponse(
        status=overall,  # type: ignore[arg-type]
        version="1.0.0",
        environment=settings.environment,
        uptime_s=round(time.time() - _start_time, 1),
        components=components,
    )
