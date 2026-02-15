"""
Дополнительные unit тесты validators — покрываем оставшиеся ветки.
"""
from __future__ import annotations

import pytest

from app.services.validators import validate_amount


@pytest.mark.unit
class TestValidateAmountEdgeCases:

    def test_none_returns_false(self) -> None:
        """line 38: amount is None → return False."""
        assert validate_amount(None) is False  # type: ignore[arg-type]

    def test_nan_returns_false(self) -> None:
        """NaN не должен проходить валидацию."""
        import math
        assert validate_amount(float("nan")) is False

    def test_infinity_returns_false(self) -> None:
        assert validate_amount(float("inf")) is False

    def test_exact_boundary_max(self) -> None:
        """Ровно 1_000_000 — должен проходить."""
        assert validate_amount(1_000_000.0) is True

    def test_one_cent_above_zero(self) -> None:
        """Минимальный валидный amount."""
        assert validate_amount(0.001) is True
