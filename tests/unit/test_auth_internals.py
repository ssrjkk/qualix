"""
Unit тесты внутренней логики auth — _create_token, _verify_token.
Покрывают все ветки: expired, malformed, invalid sig, valid.
"""

from __future__ import annotations

import hmac

import pytest

from app.api.auth import _create_token, _verify_token

SECRET = "test-secret-for-unit"


def _signed(payload: str, secret: str = SECRET) -> str:
    """Токен с валидной подписью, но произвольным payload — чтобы пройти
    проверку подписи и попасть в нужную ветку разбора."""
    sig = hmac.new(secret.encode(), payload.encode(), "sha256").hexdigest()
    return f"{payload}:{sig}"


@pytest.mark.unit
class TestCreateToken:
    def test_returns_string(self) -> None:
        token = _create_token("sergey", SECRET)
        assert isinstance(token, str)
        assert len(token) > 20

    def test_contains_username(self) -> None:
        token = _create_token("sergey", SECRET)
        assert "sergey" in token

    def test_different_secrets_produce_different_tokens(self) -> None:
        t1 = _create_token("user", "secret1")
        t2 = _create_token("user", "secret2")
        assert t1 != t2


@pytest.mark.unit
class TestVerifyToken:
    def test_valid_token_returns_username(self) -> None:
        token = _create_token("sergey", SECRET, expires_minutes=30)
        result = _verify_token(token, SECRET)
        assert result == "sergey"

    def test_wrong_secret_returns_none(self) -> None:
        token = _create_token("sergey", SECRET)
        result = _verify_token(token, "wrong-secret")
        assert result is None

    def test_expired_token_returns_none(self) -> None:
        token = _create_token("sergey", SECRET, expires_minutes=-1)
        result = _verify_token(token, SECRET)
        assert result is None

    def test_completely_malformed_token_returns_none(self) -> None:
        assert _verify_token("not.a.token.at.all", SECRET) is None

    def test_empty_string_returns_none(self) -> None:
        assert _verify_token("", SECRET) is None

    def test_garbage_bytes_returns_none(self) -> None:
        assert _verify_token("aaaa:bbbb:cccc", SECRET) is None

    def test_truncated_token_returns_none(self) -> None:
        token = _create_token("sergey", SECRET)
        truncated = token[:10]
        assert _verify_token(truncated, SECRET) is None

    def test_tampered_payload_returns_none(self) -> None:
        token = _create_token("sergey", SECRET)
        tampered = "evil_user" + token[6:]
        assert _verify_token(tampered, SECRET) is None

    def test_invalid_date_triggers_exception_branch(self) -> None:
        """Подпись валидна, но fromisoformat() бросает ValueError → except → None."""
        assert _verify_token(_signed("sergey:NOT_A_VALID_ISO_DATE"), SECRET) is None

    def test_no_colon_payload_triggers_exception_branch(self) -> None:
        """Подпись валидна, но payload.split(':',1) даёт один элемент → ValueError."""
        assert _verify_token(_signed("nocolonhere"), SECRET) is None

    @pytest.mark.parametrize("username", ["a", "bad username", "bad!user", "user/name", "x" * 65])
    def test_username_violating_pattern_is_rejected(self, username: str) -> None:
        """Подпись валидна, но username не проходит _USERNAME_RE → None."""
        payload = f"{username}:2099-01-01T00:00:00+00:00"
        assert _verify_token(_signed(payload), SECRET) is None

    def test_far_future_token_is_accepted(self) -> None:
        payload = "sergey:2099-01-01T00:00:00+00:00"
        assert _verify_token(_signed(payload), SECRET) == "sergey"

    def test_signature_mismatch_on_multi_colon_payload(self) -> None:
        """rsplit(':', 1) режет по последнему разделителю — подпись не сходится."""
        assert _verify_token(f"sergey:extra:{'ab' * 32}", SECRET) is None
