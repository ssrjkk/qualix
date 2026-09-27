"""Pydantic схемы для User."""

from __future__ import annotations

import re
from datetime import datetime
from decimal import Decimal
from typing import ClassVar

from pydantic import BaseModel, EmailStr, Field, field_validator

_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_.\-]+$")


class UserCreate(BaseModel):
    username: str = Field(min_length=2, max_length=64)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    @field_validator("username", mode="before")
    @classmethod
    def strip_username(cls, v: str) -> str:
        return v.strip()

    @field_validator("username")
    @classmethod
    def validate_username_chars(cls, v: str) -> str:
        if not _USERNAME_RE.match(v):
            raise ValueError(
                "username may only contain letters, digits, dots, hyphens, underscores"
            )
        return v

    @field_validator("email", mode="before")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        return v.lower().strip()

    @field_validator("password")
    @classmethod
    def password_complexity(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError("password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("password must contain at least one digit")
        return v


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class UserListResponse(BaseModel):
    items: list[UserResponse]
    total: int
    limit: int
    offset: int


class PaymentRequest(BaseModel):
    amount: Decimal = Field(gt=0, le=1_000_000)
    currency: str = Field(min_length=3, max_length=4)
    description: str = Field(max_length=256)

    ALLOWED_CURRENCIES: ClassVar[set[str]] = {"USD", "EUR", "RUB", "USDT", "GBP", "JPY"}

    @field_validator("currency")
    @classmethod
    def validate_currency(cls, v: str) -> str:
        upper = v.upper()
        if upper not in cls.ALLOWED_CURRENCIES:
            raise ValueError(f"Currency must be one of {cls.ALLOWED_CURRENCIES}")
        return upper
