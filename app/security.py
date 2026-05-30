"""
Password hashing — bcrypt через passlib.
SHA-256 небезопасен для паролей: нет соли, нет cost factor.
bcrypt: автоматическая соль, настраиваемый cost (rounds).
"""

from __future__ import annotations

import bcrypt


def hash_password(password: str) -> str:
    """Хешируем пароль с автоматической солью. Cost=12 (OWASP рекомендация)."""
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt).decode()


def verify_password(plain: str, hashed: str) -> bool:
    """Constant-time сравнение — защита от timing attacks."""
    try:
        return bcrypt.checkpw(plain.encode(), hashed.encode())
    except Exception:
        return False
