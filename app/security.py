"""
Password hashing — bcrypt через passlib.
SHA-256 небезопасен для паролей: нет соли, нет cost factor.
bcrypt: автоматическая соль, настраиваемый cost (rounds).

Для паролей >72 байт: сначала SHA-256, затем bcrypt полученного hex.
(OWASP рекомендует pre-hashing для обхода лимита bcrypt.)
"""

from __future__ import annotations

import hashlib

import bcrypt

MAX_BCRYPT_BYTES = 72


def _normalize_password(password: str) -> bytes:
    """Приводим пароль к формату, который можно передать в bcrypt.

    Если пароль > 72 байт в UTF-8, сначала хешируем SHA-256,
    затем используем hex-строку (64 символа, всегда < 72 байт).
    """
    raw = password.encode("utf-8")
    if len(raw) > MAX_BCRYPT_BYTES:
        return hashlib.sha256(raw).hexdigest().encode()
    return raw


def hash_password(password: str) -> str:
    """Хешируем пароль с автоматической солью. Cost=12 (OWASP рекомендация)."""
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(_normalize_password(password), salt).decode()


def verify_password(plain: str, hashed: str) -> bool:
    """Constant-time сравнение — защита от timing attacks."""
    try:
        return bcrypt.checkpw(_normalize_password(plain), hashed.encode())
    except Exception:
        return False
