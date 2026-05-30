"""
Unit тесты внутренней логики auth — _create_token, _verify_token.
Покрывают все ветки: expired, malformed, invalid sig, valid.
"""

from __future__ import annotations

import pytest

from app.api.auth import _create_token, _verify_token

SECRET = "test-secret-for-unit"


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
        # line 43: sig != expected → return None
        result = _verify_token(token, "wrong-secret")
        assert result is None

    def test_expired_token_returns_none(self) -> None:
        # line 47: datetime.now(utc) > expires → return None
        token = _create_token("sergey", SECRET, expires_minutes=-1)
        result = _verify_token(token, SECRET)
        assert result is None

    def test_completely_malformed_token_returns_none(self) -> None:
        # line 49-50: Exception → return None
        assert _verify_token("not.a.token.at.all", SECRET) is None

    def test_empty_string_returns_none(self) -> None:
        # line 49-50: Exception on split
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
        """lines 49-50: fromisoformat() бросает ValueError → except Exception."""
        import hashlib

        payload = "sergey:NOT_A_VALID_ISO_DATE"
        sig = hashlib.sha256(f"{payload}:{SECRET}".encode()).hexdigest()
        token = f"{payload}:{sig}"
        assert _verify_token(token, SECRET) is None

    def test_no_colon_payload_triggers_exception_branch(self) -> None:
        """username, expires_str = payload.split(':',1) — один элемент → ValueError."""
        import hashlib

        payload = "nocolonhere"
        sig = hashlib.sha256(f"{payload}:{SECRET}".encode()).hexdigest()
        token = f"{payload}:{sig}"
        assert _verify_token(token, SECRET) is None
