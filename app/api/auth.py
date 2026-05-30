"""Auth router — JWT login/logout."""

from __future__ import annotations

import hashlib
from datetime import UTC, datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import Settings
from app.dependencies import get_db, get_settings
from app.repositories.user_repo import UserRepository
from app.security import verify_password

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


def _create_token(username: str, secret: str, expires_minutes: int = 30) -> str:
    """Минималистичный токен для тестового SUT (не production)."""
    expires = datetime.now(UTC) + timedelta(minutes=expires_minutes)
    payload = f"{username}:{expires.isoformat()}"
    sig = hashlib.sha256(f"{payload}:{secret}".encode()).hexdigest()
    return f"{payload}:{sig}"


def _verify_token(token: str, secret: str) -> str | None:
    """Вернуть username если токен валиден, иначе None."""
    try:
        parts = token.rsplit(":", 1)
        payload, sig = ":".join(parts[:-1]), parts[-1]
        expected = hashlib.sha256(f"{payload}:{secret}".encode()).hexdigest()
        if sig != expected:
            return None
        username, expires_str = payload.split(":", 1)
        expires = datetime.fromisoformat(expires_str)
        if datetime.now(UTC) > expires:
            return None
        return username
    except Exception:
        return None


@router.post("/login", response_model=TokenResponse)
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> TokenResponse:
    # Специальные тестовые пользователи
    test_users = {
        "test_user": "test_pass",
        "admin": "admin_pass",
        "load_user": "pass",
    }
    if data.username in test_users and test_users[data.username] == data.password:
        token = _create_token(
            data.username, settings.secret_key, settings.access_token_expire_minutes
        )
        return TokenResponse(access_token=token)

    repo = UserRepository(db)
    user = await repo.get_by_email(data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = _create_token(user.username, settings.secret_key, settings.access_token_expire_minutes)
    return TokenResponse(access_token=token)
