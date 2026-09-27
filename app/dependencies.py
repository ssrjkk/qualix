"""FastAPI dependencies."""

from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import Any

from fastapi import Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import Settings

# Переопределяется через create_app для тестов
_test_settings: Settings | None = None
_shared_engine: AsyncEngine | None = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def get_settings() -> Settings:
    if _test_settings is not None:
        return _test_settings
    return Settings()


def get_engine(settings: Settings) -> AsyncEngine:
    global _shared_engine
    if _shared_engine is not None:
        return _shared_engine
    connect_args = {"check_same_thread": False} if "sqlite" in settings.database_url else {}
    _shared_engine = create_async_engine(
        settings.database_url, connect_args=connect_args, echo=False
    )
    return _shared_engine


async def get_db(
    settings: Settings = Depends(get_settings),
) -> AsyncGenerator[AsyncSession, None]:
    global _session_factory
    engine = get_engine(settings)
    if _session_factory is None:
        _session_factory = async_sessionmaker(engine, expire_on_commit=False, autoflush=False)
    async with _session_factory() as session:
        yield session


async def get_current_user(
    authorization: str = Header(default=""),
    settings: Settings = Depends(get_settings),
) -> dict[str, Any]:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    token = authorization.removeprefix("Bearer ")
    from app.api.auth import _verify_token

    username = _verify_token(token, settings.secret_key)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"username": username}
