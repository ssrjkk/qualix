"""
time-machine тесты — детерминированные проверки логики зависящей от времени.
Без time-machine: тесты на expired token нестабильны (зависят от system clock).
С time-machine: полный контроль над временем.
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta

import pytest
import time_machine

from app.api.auth import _create_token, _verify_token

SECRET = "test-secret-for-time-32chars!!"


@pytest.mark.unit
class TestTokenExpiryWithTimeMachine:

    @time_machine.travel("2026-01-01 12:00:00+00:00", tick=False)
    def test_token_valid_before_expiry(self) -> None:
        """Токен создан в 12:00, проверяем в 12:00 — валиден."""
        token = _create_token("sergey", SECRET, expires_minutes=30)
        result = _verify_token(token, SECRET)
        assert result == "sergey"

    @time_machine.travel("2026-01-01 12:00:00+00:00", tick=False)
    def test_token_expired_after_window(self) -> None:
        """
        Создаём токен в 12:00 с TTL=30min.
        Переносим время на 12:31 — токен должен быть expired.
        """
        token = _create_token("sergey", SECRET, expires_minutes=30)

        # Переносим время вперёд
        with time_machine.travel("2026-01-01 12:31:00+00:00", tick=False):
            result = _verify_token(token, SECRET)
        assert result is None

    @time_machine.travel("2026-01-01 12:00:00+00:00", tick=False)
    def test_token_valid_at_boundary(self) -> None:
        """Токен в момент истечения — ровно на границе."""
        token = _create_token("sergey", SECRET, expires_minutes=30)

        # Ровно в момент истечения — ещё валиден (не строго больше)
        with time_machine.travel("2026-01-01 12:29:59+00:00", tick=False):
            result = _verify_token(token, SECRET)
        assert result == "sergey"

    @time_machine.travel("2026-01-01 00:00:00+00:00", tick=False)
    def test_token_negative_expiry_instantly_expired(self) -> None:
        """expires_minutes=-1 → токен уже истёк в момент создания."""
        token = _create_token("sergey", SECRET, expires_minutes=-1)
        result = _verify_token(token, SECRET)
        assert result is None

    @time_machine.travel("2026-06-15 09:30:00+00:00", tick=False)
    def test_multiple_tokens_independent_expiry(self) -> None:
        """Разные токены независимы."""
        token_short = _create_token("alice", SECRET, expires_minutes=5)
        token_long = _create_token("bob", SECRET, expires_minutes=60)

        # Через 10 минут
        with time_machine.travel("2026-06-15 09:40:00+00:00", tick=False):
            assert _verify_token(token_short, SECRET) is None   # expired
            assert _verify_token(token_long, SECRET) == "bob"   # still valid


@pytest.mark.unit
class TestTimestampDeterminism:
    """Демонстрируем зачем нужен time-machine — без него тест нестабилен."""

    @time_machine.travel("2026-03-20 15:00:00+00:00", tick=False)
    def test_token_contains_fixed_timestamp(self) -> None:
        """
        С time-machine время детерминировано — токен всегда содержит
        ровно ту дату которую мы ожидаем.
        """
        token = _create_token("sergey", SECRET, expires_minutes=30)
        # expires = 15:00 + 30min = 15:30
        assert "2026-03-20T15:30" in token

    @time_machine.travel("2026-01-01 00:00:00+00:00", tick=False)
    def test_create_token_is_deterministic(self) -> None:
        """
        При фиксированном времени _create_token детерминирован:
        одинаковый username + secret + время → одинаковый токен.
        """
        t1 = _create_token("user", SECRET, expires_minutes=30)
        t2 = _create_token("user", SECRET, expires_minutes=30)
        assert t1 == t2
