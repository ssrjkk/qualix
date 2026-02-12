"""
Валидаторы бизнес-логики.
Чистые функции — нет IO-зависимостей.
"""
from __future__ import annotations

import re

import email_validator as ev

_PHONE_RE = re.compile(r"^\+?[1-9]\d{6,14}$")
_SCRIPT_RE = re.compile(r"<script[\s\S]*?>[\s\S]*?</script>", re.IGNORECASE)
_HTML_TAG_RE = re.compile(r"<[^>]+>")

MAX_AMOUNT = 1_000_000.0


def validate_email(email: str) -> bool:
    """RFC 5321/5322 валидация через email-validator."""
    if not email or len(email) > 254:
        return False
    try:
        ev.validate_email(email, check_deliverability=False)
        return True
    except ev.EmailNotValidError:
        return False


def validate_phone(phone: str) -> bool:
    if not phone:
        return False
    digits_only = re.sub(r"[\s\-()]", "", phone)
    return bool(_PHONE_RE.match(digits_only))


def validate_amount(amount: float) -> bool:
    if amount is None:
        return False
    return 0.0 < amount <= MAX_AMOUNT


def sanitize_string(s: str) -> str:
    """Удаляет script-теги и HTML-теги. Идемпотентна."""
    s = _SCRIPT_RE.sub("", s)
    s = _HTML_TAG_RE.sub("", s)
    return s
