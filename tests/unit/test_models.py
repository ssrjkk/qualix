"""Unit тесты Pydantic моделей — валидация, нормализация, rejection."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.models.user import PaymentRequest, UserCreate


class TestUserCreate:
    @pytest.mark.unit
    def test_valid_user_passes(self) -> None:
        u = UserCreate(username="sergey_qa", email="ray013lefe@gmail.com", password="ValidPass1!")
        assert u.username == "sergey_qa"
        assert u.email == "ray013lefe@gmail.com"

    @pytest.mark.unit
    def test_email_normalized_to_lowercase(self) -> None:
        u = UserCreate(username="usr", email="TEST@EXAMPLE.COM", password="ValidPass1!")
        assert u.email == "test@example.com"

    @pytest.mark.unit
    def test_username_stripped(self) -> None:
        u = UserCreate(username="  spacey  ", email="a@b.com", password="ValidPass1!")
        assert u.username == "spacey"

    @pytest.mark.unit
    @pytest.mark.parametrize(
        ("password", "match"),
        [
            ("short1A", ""),  # too short
            ("nouppercase1!", "uppercase"),
            ("NODIGIT!abc", "digit"),
            ("a" * 129, ""),  # too long
        ],
    )
    def test_invalid_passwords_rejected(self, password: str, match: str) -> None:
        with pytest.raises(ValidationError) as exc:
            UserCreate(username="usr", email="a@b.com", password=password)
        if match:
            assert match in str(exc.value).lower()

    @pytest.mark.unit
    @pytest.mark.parametrize("field", ["username", "email", "password"])
    def test_missing_required_field_raises(self, field: str) -> None:
        data = {"username": "u", "email": "a@b.com", "password": "ValidPass1!"}
        del data[field]
        with pytest.raises(ValidationError):
            UserCreate(**data)

    @pytest.mark.unit
    def test_username_too_short_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserCreate(username="x", email="a@b.com", password="ValidPass1!")

    @pytest.mark.unit
    def test_username_too_long_raises(self) -> None:
        with pytest.raises(ValidationError):
            UserCreate(username="a" * 65, email="a@b.com", password="ValidPass1!")


class TestPaymentRequest:
    @pytest.mark.unit
    @pytest.mark.parametrize("currency", ["USD", "EUR", "RUB", "USDT", "GBP", "JPY"])
    def test_valid_currencies(self, currency: str) -> None:
        p = PaymentRequest(amount=100.0, currency=currency, description="ok")
        assert p.currency == currency

    @pytest.mark.unit
    @pytest.mark.parametrize("currency", ["lol", "XRP", "DOGE", "BTC"])
    def test_invalid_currencies_rejected(self, currency: str) -> None:
        with pytest.raises(ValidationError):
            PaymentRequest(amount=100.0, currency=currency, description="bad")

    @pytest.mark.unit
    @pytest.mark.parametrize("amount", [0.0, -1.0, -0.001])
    def test_non_positive_amount_rejected(self, amount: float) -> None:
        with pytest.raises(ValidationError):
            PaymentRequest(amount=amount, currency="USD", description="bad")

    @pytest.mark.unit
    def test_over_max_amount_rejected(self) -> None:
        with pytest.raises(ValidationError):
            PaymentRequest(amount=1_000_001.0, currency="USD", description="bad")

    @pytest.mark.unit
    def test_currency_case_insensitive(self) -> None:
        p = PaymentRequest(amount=1.0, currency="usd", description="ok")
        assert p.currency == "USD"
