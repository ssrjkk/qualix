"""Auth router — JWT login/logout."""

from __future__ import annotations

import hmac
import re
from datetime import UTC, datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import Settings
from app.dependencies import get_db, get_settings
from app.repositories.user_repo import UserRepository
from app.security import verify_password

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_.-]{2,64}$")


class LoginRequest(BaseModel):
    username: str = Field(min_length=1, max_length=128)
    password: str = Field(min_length=1, max_length=256)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


def _create_token(username: str, secret: str, expires_minutes: int = 30) -> str:
    """HMAC-SHA256 token for SUT."""
    expires = datetime.now(UTC) + timedelta(minutes=expires_minutes)
    payload = f"{username}:{expires.isoformat()}"
    sig = hmac.new(secret.encode(), payload.encode(), "sha256").hexdigest()
    return f"{payload}:{sig}"


def _verify_token(token: str, secret: str) -> str | None:
    """Return username if token is valid, else None."""
    try:
        parts = token.rsplit(":", 1)
        if len(parts) != 2:
            return None
        payload, sig = parts
        expected = hmac.new(secret.encode(), payload.encode(), "sha256").hexdigest()
        if not hmac.compare_digest(sig, expected):
            return None
        username, expires_str = payload.split(":", 1)
        if not _USERNAME_RE.match(username):
            return None
        expires = datetime.fromisoformat(expires_str)
        if datetime.now(UTC) > expires:
            return None
        return username
    except (ValueError, IndexError):
        return None


@router.post("/login", response_model=TokenResponse)
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> TokenResponse:
    if settings.environment in ("test", "development"):
        test_users = {
            "test_user": "test_pass",
            "admin": "admin_pass",
            "load_user": "pass",
        }
        expected_pw = test_users.get(data.username)
        if expected_pw is not None and hmac.compare_digest(expected_pw, data.password):
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
