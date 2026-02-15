"""
Unit тесты dependencies.py — покрываем get_settings без _test_settings.
"""
from __future__ import annotations

import pytest


@pytest.mark.unit
class TestGetSettings:

    def test_get_settings_without_override_returns_defaults(self) -> None:
        """line 24: return Settings() — когда _test_settings is None."""
        import app.dependencies as deps
        original = deps._test_settings
        try:
            deps._test_settings = None
            settings = deps.get_settings()
            # должен вернуть Settings с дефолтными значениями
            assert settings is not None
            assert hasattr(settings, "database_url")
            assert hasattr(settings, "secret_key")
        finally:
            deps._test_settings = original  # восстанавливаем

    def test_get_settings_with_override_returns_override(self) -> None:
        """line 22-23: _test_settings is not None → return it."""
        import app.dependencies as deps
        from app.config import Settings
        original = deps._test_settings
        try:
            custom = Settings(secret_key="custom-secret-for-test-32!")
            deps._test_settings = custom
            result = deps.get_settings()
            assert result is custom
        finally:
            deps._test_settings = original

    def test_get_engine_creates_engine(self) -> None:
        """get_engine возвращает AsyncEngine."""
        import app.dependencies as deps
        from app.config import Settings
        original_engine = deps._shared_engine
        try:
            deps._shared_engine = None
            settings = Settings(
                database_url="sqlite+aiosqlite:///./tmp_engine_test.db"
            )
            engine = deps.get_engine(settings)
            assert engine is not None
            assert deps._shared_engine is engine  # singleton установлен
        finally:
            deps._shared_engine = original_engine
            import os
            if os.path.exists("./tmp_engine_test.db"):
                os.remove("./tmp_engine_test.db")

    def test_get_engine_returns_same_instance(self) -> None:
        """get_engine singleton — повторный вызов возвращает тот же engine."""
        import app.dependencies as deps
        from app.config import Settings
        original_engine = deps._shared_engine
        try:
            deps._shared_engine = None
            settings = Settings(
                database_url="sqlite+aiosqlite:///./tmp_engine_test2.db"
            )
            e1 = deps.get_engine(settings)
            e2 = deps.get_engine(settings)
            assert e1 is e2
        finally:
            deps._shared_engine = original_engine
            import os
            for f in ["./tmp_engine_test2.db"]:
                if os.path.exists(f):
                    os.remove(f)
