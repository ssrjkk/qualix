"""FastAPI application factory."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import OperationalError

from app.config import Settings
from app.logging_config import configure_logging, get_logger
from app.models.db import Base

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    settings: Settings = app.state.settings
    configure_logging(settings.environment)
    logger.info("app_starting", environment=settings.environment)

    from app.dependencies import get_engine

    engine = get_engine(settings)

    max_retries = 5
    for attempt in range(1, max_retries + 1):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            break
        except OperationalError as e:
            if attempt == max_retries:
                logger.error("db_connection_failed", max_retries=max_retries, error=str(e))
                raise
            wait = 2 ** attempt
            logger.warning(
                "db_connection_retry",
                attempt=attempt,
                max_retries=max_retries,
                wait_s=wait,
                error=str(e),
            )
            await asyncio.sleep(wait)

    logger.info("app_started")
    yield
    logger.info("app_stopping")


def create_app(settings: Settings | None = None) -> FastAPI:
    if settings is None:
        settings = Settings()

    import app.dependencies as deps

    deps._test_settings = settings
    deps._shared_engine = None

    application = FastAPI(
        title="QA Sentinel",
        version="1.0.0",
        description="Full-stack QA automation platform",
        lifespan=lifespan,
    )
    application.state.settings = settings

    # ── Middleware (порядок важен: первый добавленный — последний выполняется) ─
    from app.middleware import LoggingMiddleware, RateLimitMiddleware, RequestIDMiddleware

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"] if settings.environment != "production" else [],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    rate_limit = 10000 if settings.environment == "test" else 100
    application.add_middleware(RateLimitMiddleware, limit=rate_limit, window=60.0)
    application.add_middleware(LoggingMiddleware)
    application.add_middleware(RequestIDMiddleware)

    # ── Routers ───────────────────────────────────────────────────────────────
    from app.api.auth import router as auth_router
    from app.api.health import router as health_router
    from app.api.users import router as users_router

    application.include_router(health_router)
    application.include_router(auth_router)
    application.include_router(users_router)

    # Фронтенд — serve static files
    from pathlib import Path

    frontend_path = Path(__file__).parent.parent / "frontend"
    if frontend_path.exists():  # pragma: no branch
        from fastapi.responses import FileResponse
        from fastapi.staticfiles import StaticFiles

        _html = str(frontend_path / "index.html")

        @application.get("/login", include_in_schema=False)
        async def login_page() -> FileResponse:
            return FileResponse(_html)

        @application.get("/dashboard", include_in_schema=False)
        async def dashboard_page() -> FileResponse:
            return FileResponse(_html)

        application.mount(
            "/",
            StaticFiles(directory=str(frontend_path), html=True),
            name="frontend",
        )

    return application


app = create_app()
