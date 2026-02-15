"""
Unit тесты + Hypothesis property-based.
Нет IO, нет фикстур из conftest — запускаются мгновенно.
"""
from __future__ import annotations

import pytest
from hypothesis import given, settings as h_settings, HealthCheck
from hypothesis import strategies as st

from app.services.validators import (
    validate_email,
    validate_phone,
    validate_amount,
    sanitize_string,
)


class TestEmailValidator:

    @pytest.mark.unit
    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("user+tag@sub.domain.io", True),
        ("a@b.co", True),
        ("userexample.com", False),
        ("missing@", False),
        ("@nodomain.com", False),
        ("", False),
        ("a" * 250 + "@x.com", False),
        ("two@@domain.com", False),
    ])
    def test_parametrized(self, email: str, expected: bool) -> None:
        assert validate_email(email) is expected

    @pytest.mark.unit
    @given(st.emails())
    @h_settings(max_examples=500, suppress_health_check=[HealthCheck.too_slow])
    def test_hypothesis_generated_emails_are_valid(self, email: str) -> None:
        assert validate_email(email) is True

    @pytest.mark.unit
    @given(st.text(min_size=1, max_size=80).filter(lambda s: "@" not in s))
    def test_hypothesis_no_at_symbol_always_invalid(self, s: str) -> None:
        assert validate_email(s) is False


class TestPhoneValidator:

    @pytest.mark.unit
    @pytest.mark.parametrize("phone,expected", [
        ("+79161234567", True),
        ("79161234567", True),
        ("+1 (800) 555-1234", True),
        ("", False),
        ("abc", False),
        ("123", False),  # too short
    ])
    def test_parametrized(self, phone: str, expected: bool) -> None:
        assert validate_phone(phone) is expected


class TestAmountValidator:

    @pytest.mark.unit
    @pytest.mark.parametrize("amount,expected", [
        (0.01, True),
        (1.0, True),
        (999_999.99, True),
        (1_000_000.0, True),
        (0.0, False),
        (-1.0, False),
        (1_000_000.01, False),
    ])
    def test_boundaries(self, amount: float, expected: bool) -> None:
        assert validate_amount(amount) is expected

    @pytest.mark.unit
    @given(st.floats(min_value=0.01, max_value=1_000_000.0, allow_nan=False, allow_infinity=False))
    def test_hypothesis_valid_range_always_passes(self, amount: float) -> None:
        assert validate_amount(amount) is True

    @pytest.mark.unit
    @given(st.floats(max_value=-0.001, allow_nan=False, allow_infinity=False))
    def test_hypothesis_negative_always_fails(self, amount: float) -> None:
        assert validate_amount(amount) is False


class TestSanitizeString:

    @pytest.mark.unit
    def test_removes_script_tag(self) -> None:
        result = sanitize_string("<script>alert('xss')</script>hello")
        assert "<script>" not in result.lower()
        assert "hello" in result

    @pytest.mark.unit
    def test_removes_html_tags(self) -> None:
        result = sanitize_string("<b>bold</b>")
        assert "<b>" not in result
        assert "bold" in result

    @pytest.mark.unit
    @given(st.text(max_size=500))
    def test_hypothesis_no_script_tags_after_sanitize(self, s: str) -> None:
        result = sanitize_string(s)
        assert "<script>" not in result.lower()
        assert "</script>" not in result.lower()

    @pytest.mark.unit
    @given(st.text(max_size=500))
    def test_hypothesis_idempotent(self, s: str) -> None:
        assert sanitize_string(sanitize_string(s)) == sanitize_string(s)
