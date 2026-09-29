"""Unit тесты security.py — bcrypt hashing."""

from __future__ import annotations

import pytest

from app.security import hash_password, verify_password


@pytest.mark.unit
class TestHashPassword:
    def test_returns_bcrypt_string(self) -> None:
        result = hash_password("TestPass1!")
        assert result.startswith("$2b$")

    def test_unique_salt_each_call(self) -> None:
        h1 = hash_password("SamePass1!")
        h2 = hash_password("SamePass1!")
        assert h1 != h2  # разная соль каждый раз

    def test_rounds_12(self) -> None:
        result = hash_password("TestPass1!")
        # bcrypt format: $2b$12$...
        assert "$12$" in result


@pytest.mark.unit
class TestVerifyPassword:
    def test_correct_password_returns_true(self) -> None:
        hashed = hash_password("CorrectPass1!")
        assert verify_password("CorrectPass1!", hashed) is True

    def test_wrong_password_returns_false(self) -> None:
        hashed = hash_password("RealPass1!")
        assert verify_password("WrongPass1!", hashed) is False

    def test_invalid_hash_returns_false(self) -> None:
        # невалидный хеш → False, без исключения
        assert verify_password("anypass", "not_a_valid_bcrypt_hash") is False

    def test_empty_hash_returns_false(self) -> None:
        assert verify_password("anypass", "") is False

    def test_empty_password_against_valid_hash(self) -> None:
        hashed = hash_password("RealPass1!")
        assert verify_password("", hashed) is False

    def test_constant_time_both_paths_return_bool(self) -> None:
        """verify_password всегда возвращает bool — не выбрасывает исключений."""
        hashed = hash_password("Pass1!")
        result_correct = verify_password("Pass1!", hashed)
        result_wrong = verify_password("Wrong1!", hashed)
        assert isinstance(result_correct, bool)
        assert isinstance(result_wrong, bool)


@pytest.mark.unit
class TestLongPasswordNormalization:
    """bcrypt молча обрезает всё после 72 байта — это дыра, если длинные
    пароли не нормализовать заранее."""

    def test_over_72_bytes_roundtrip(self) -> None:
        long_pw = "A1" * 50  # 100 байт ASCII
        assert verify_password(long_pw, hash_password(long_pw)) is True

    def test_multibyte_over_72_bytes_roundtrip(self) -> None:
        long_pw = "пароль" * 20  # UTF-8: 120 байт при 40 символах
        hashed = hash_password(long_pw)
        assert verify_password(long_pw, hashed) is True
        assert verify_password("пароль" * 19, hashed) is False

    def test_passwords_sharing_72_byte_prefix_are_distinguished(self) -> None:
        first = "A" * 72 + "alpha1!"
        second = "A" * 72 + "beta2!!"
        hashed = hash_password(first)
        assert verify_password(first, hashed) is True
        assert verify_password(second, hashed) is False, (
            "prefix beyond 72 bytes was ignored — password is effectively truncated"
        )

    def test_exactly_72_bytes_passes_through_unchanged(self) -> None:
        pw = "A1" * 36  # ровно 72 байт
        assert verify_password(pw, hash_password(pw)) is True

    def test_long_password_hash_is_valid_bcrypt(self) -> None:
        assert hash_password("x1" * 200).startswith("$2b$12$")
