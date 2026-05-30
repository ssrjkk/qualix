"""
pytest-benchmark — performance тесты критических функций.
Цель: выявить регрессии производительности до попадания в прод.
Запуск: pytest tests/unit/test_performance.py --benchmark-only
"""

from __future__ import annotations

from datetime import UTC

import pytest

# ── Password hashing ─────────────────────────────────────────────────────────


@pytest.mark.unit
def test_benchmark_hash_password(benchmark) -> None:  # type: ignore[no-untyped-def]
    """
    bcrypt hash должен занимать ~100-300ms при rounds=12.
    Если быстрее — rounds снижен (небезопасно).
    Если медленнее 1s — деградация производительности.
    """
    from app.security import hash_password

    result = benchmark(hash_password, "BenchmarkPass1!")
    assert result.startswith("$2b$")


@pytest.mark.unit
def test_benchmark_verify_password(benchmark) -> None:  # type: ignore[no-untyped-def]
    """verify_password должен быть constant-time — ~100-300ms."""
    from app.security import hash_password, verify_password

    hashed = hash_password("BenchmarkPass1!")
    result = benchmark(verify_password, "BenchmarkPass1!", hashed)
    assert result is True


@pytest.mark.unit
def test_benchmark_verify_wrong_password(benchmark) -> None:  # type: ignore[no-untyped-def]
    """
    Неверный пароль должен занимать столько же времени что и верный.
    Constant-time — защита от timing attacks.
    """
    from app.security import hash_password, verify_password

    hashed = hash_password("BenchmarkPass1!")
    result = benchmark(verify_password, "WrongPassword1!", hashed)
    assert result is False


# ── Token creation / verification ────────────────────────────────────────────


@pytest.mark.unit
def test_benchmark_create_token(benchmark) -> None:  # type: ignore[no-untyped-def]
    """Token creation — должен быть < 1ms (HMAC-SHA256 быстрый)."""
    from app.api.auth import _create_token

    result = benchmark(_create_token, "sergey", "test-secret-32chars!", 30)
    assert len(result) > 20


@pytest.mark.unit
def test_benchmark_verify_token(benchmark) -> None:  # type: ignore[no-untyped-def]
    """Token verification — должен быть < 1ms."""
    from app.api.auth import _create_token, _verify_token

    token = _create_token("sergey", "test-secret-32chars!", 30)
    result = benchmark(_verify_token, token, "test-secret-32chars!")
    assert result == "sergey"


# ── Validators ───────────────────────────────────────────────────────────────


@pytest.mark.unit
def test_benchmark_validate_email(benchmark) -> None:  # type: ignore[no-untyped-def]
    """Email валидация через email-validator — должна быть < 5ms."""
    from app.services.validators import validate_email

    result = benchmark(validate_email, "user@example.com")
    assert result is True


@pytest.mark.unit
def test_benchmark_sanitize_string(benchmark) -> None:  # type: ignore[no-untyped-def]
    """Санитизация строки — должна быть < 1ms для типичного ввода."""
    from app.services.validators import sanitize_string

    dirty = "<script>alert('xss')</script>" + "Hello world! " * 100
    result = benchmark(sanitize_string, dirty)
    assert "<script>" not in result.lower()


@pytest.mark.unit
def test_benchmark_validate_amount(benchmark) -> None:  # type: ignore[no-untyped-def]
    """Amount валидация — должна быть < 0.1ms (простое сравнение)."""
    from app.services.validators import validate_amount

    result = benchmark(validate_amount, 999.99)
    assert result is True


# ── Pydantic model parsing ────────────────────────────────────────────────────


@pytest.mark.unit
def test_benchmark_user_create_model(benchmark) -> None:  # type: ignore[no-untyped-def]
    """Pydantic UserCreate parsing — должен быть < 1ms."""
    from app.models.user import UserCreate

    def parse() -> UserCreate:
        return UserCreate(
            username="benchmark_user",
            email="bench@example.com",
            password="BenchPass1!",
        )

    result = benchmark(parse)
    assert result.username == "benchmark_user"


@pytest.mark.unit
def test_benchmark_user_response_model(benchmark) -> None:  # type: ignore[no-untyped-def]
    """UserResponse.model_validate из ORM — должен быть < 0.5ms."""
    from datetime import datetime

    from app.models.db import UserORM
    from app.models.user import UserResponse

    u = UserORM()
    u.id = 1
    u.username = "bench"
    u.email = "bench@t.com"
    u.is_active = True
    u.created_at = datetime.now(UTC)
    u.updated_at = datetime.now(UTC)

    result = benchmark(UserResponse.model_validate, u)
    assert result.id == 1
