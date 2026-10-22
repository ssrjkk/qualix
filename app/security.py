"""
Password hashing — bcrypt через passlib.
SHA-256 небезопасен для паролей: нет соли, нет cost factor.
bcrypt: автоматическая соль, настраиваемый cost (rounds).

Для паролей >72 байт: сначала SHA-256, затем bcrypt полученного hex.
(OWASP рекомендует pre-hashing для обхода лимита bcrypt.)
"""

from __future__ import annotations

import hashlib
import os

import bcrypt

MAX_BCRYPT_BYTES = 72

# Cost 12 — рекомендация OWASP для продакшена. В тестовом стеке
# (docker-compose) он понижается через BCRYPT_ROUNDS: нагрузочный тест
# должен мерить API и БД, а не стоимость KDF на двух ядрах раннера.
DEFAULT_BCRYPT_ROUNDS = 12
MIN_BCRYPT_ROUNDS = 4
MAX_BCRYPT_ROUNDS = 15


def _bcrypt_rounds() -> int:
    raw = os.getenv("BCRYPT_ROUNDS", str(DEFAULT_BCRYPT_ROUNDS))
    try:
        rounds = int(raw)
    except ValueError:
        return DEFAULT_BCRYPT_ROUNDS
    return max(MIN_BCRYPT_ROUNDS, min(MAX_BCRYPT_ROUNDS, rounds))


BCRYPT_ROUNDS = _bcrypt_rounds()


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
    """Хешируем пароль с автоматической солью.

    Cost по умолчанию 12 (OWASP рекомендация), переопределяется через
    переменную окружения BCRYPT_ROUNDS — это нужно нагрузочному тесту,
    где стоимость KDF съедает CPU раннера и искажает замеры API.
    """
    salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
    return bcrypt.hashpw(_normalize_password(password), salt).decode()


def verify_password(plain: str, hashed: str) -> bool:
    """Constant-time сравнение — защита от timing attacks."""
    try:
        return bcrypt.checkpw(_normalize_password(plain), hashed.encode())
    except (ValueError, TypeError):
        return False
