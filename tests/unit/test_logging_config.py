"""Unit тесты logging_config.py."""

from __future__ import annotations

import pytest

from app.logging_config import configure_logging, get_logger


@pytest.mark.unit
class TestConfigureLogging:
    def test_development_mode(self) -> None:
        """Не падает при вызове с environment=development."""
        configure_logging("development")
        logger = get_logger("test")
        assert logger is not None

    def test_production_mode(self) -> None:
        """line 19: environment == 'production' → JSONRenderer."""
        configure_logging("production")
        logger = get_logger("test")
        assert logger is not None

    def test_get_logger_returns_bound_logger(self) -> None:
        configure_logging("test")
        logger = get_logger("my_module")
        assert logger is not None

    def test_get_logger_different_names(self) -> None:
        l1 = get_logger("module_a")
        l2 = get_logger("module_b")
        assert l1 is not None
        assert l2 is not None
