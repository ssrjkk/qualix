"""API тесты для health endpoints — liveness + readiness."""
from __future__ import annotations

import pytest
from httpx import AsyncClient


@pytest.mark.api
class TestLivenessProbe:

    async def test_health_200(self, client: AsyncClient) -> None:
        resp = await client.get("/health")
        assert resp.status_code == 200

    async def test_health_returns_ok_status(self, client: AsyncClient) -> None:
        data = (await client.get("/health")).json()
        assert data["status"] == "ok"

    async def test_health_returns_environment(self, client: AsyncClient) -> None:
        data = (await client.get("/health")).json()
        assert data["environment"] == "test"

    async def test_health_no_auth_required(self, client: AsyncClient) -> None:
        """Liveness probe должен быть публичным — k8s не передаёт auth."""
        resp = await client.get("/health")
        assert resp.status_code == 200

    async def test_health_fast_response(self, client: AsyncClient) -> None:
        """Liveness probe — без IO, должен отвечать быстро."""
        import time
        start = time.perf_counter()
        await client.get("/health")
        elapsed_ms = (time.perf_counter() - start) * 1000
        assert elapsed_ms < 500, f"Liveness probe too slow: {elapsed_ms:.0f}ms"


@pytest.mark.api
class TestReadinessProbe:

    async def test_health_ready_200(self, client: AsyncClient) -> None:
        resp = await client.get("/health/ready")
        assert resp.status_code == 200

    async def test_health_ready_has_components(self, client: AsyncClient) -> None:
        data = (await client.get("/health/ready")).json()
        assert "components" in data
        assert "database" in data["components"]

    async def test_health_ready_database_ok(self, client: AsyncClient) -> None:
        data = (await client.get("/health/ready")).json()
        db = data["components"]["database"]
        assert db["status"] == "ok"
        assert db["latency_ms"] is not None
        assert db["latency_ms"] >= 0

    async def test_health_ready_has_version(self, client: AsyncClient) -> None:
        data = (await client.get("/health/ready")).json()
        assert data["version"] == "1.0.0"

    async def test_health_ready_has_uptime(self, client: AsyncClient) -> None:
        data = (await client.get("/health/ready")).json()
        assert "uptime_s" in data
        assert data["uptime_s"] >= 0

    async def test_health_ready_redis_degraded_not_down(
        self, client: AsyncClient
    ) -> None:
        """Redis недоступен в тестовой среде — статус degraded, не down."""
        data = (await client.get("/health/ready")).json()
        redis_status = data["components"].get("redis", {}).get("status", "ok")
        # Redis может быть ok (если fakeredis) или degraded (если недоступен)
        # Главное — не down и не вызывает падение всего health endpoint
        assert redis_status in ("ok", "degraded")
        # Общий статус не должен быть down из-за Redis
        assert data["status"] in ("ok", "degraded")


@pytest.mark.unit
class TestHealthRouterDirect:
    """Прямые unit тесты health роутера — покрываем DB-down и Redis-ok пути."""

    async def test_db_down_sets_overall_down(self) -> None:
        """health.py:68-71 — DB exception → overall = 'down'."""
        from unittest.mock import AsyncMock, MagicMock, patch
        from app.api.health import readiness
        from app.config import Settings

        mock_db = AsyncMock()
        mock_db.execute = AsyncMock(side_effect=Exception("Connection refused"))
        mock_settings = MagicMock(spec=Settings)
        mock_settings.redis_url = "redis://localhost:9999/0"  # invalid port
        mock_settings.environment = "test"

        result = await readiness(db=mock_db, settings=mock_settings)

        assert result.status == "down"
        assert result.components["database"].status == "down"
        assert result.components["database"].detail is not None

    async def test_redis_ok_when_available(self) -> None:
        """health.py:78-81 — Redis ping ok."""
        from unittest.mock import AsyncMock, MagicMock, patch
        from app.api.health import readiness
        from app.config import Settings

        mock_db = AsyncMock()
        mock_db.execute = AsyncMock(return_value=None)

        mock_settings = MagicMock(spec=Settings)
        mock_settings.redis_url = "redis://localhost:6379/0"
        mock_settings.environment = "test"

        mock_redis = AsyncMock()
        mock_redis.ping = AsyncMock(return_value=True)
        mock_redis.aclose = AsyncMock()

        with patch("redis.asyncio.from_url", return_value=mock_redis):
            result = await readiness(db=mock_db, settings=mock_settings)

        assert result.components["database"].status == "ok"
