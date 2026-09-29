"""Unit тесты app/config.py — Defaults и валидация secret_key."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.config import Settings


@pytest.mark.unit
class TestSecretKeyValidation:
    def test_empty_secret_rejected_in_production(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("SECRET_KEY", raising=False)
        with pytest.raises(ValidationError, match="secret_key must be set"):
            Settings(environment="production", secret_key="")

    def test_placeholder_secret_rejected_in_production(self) -> None:
        with pytest.raises(ValidationError, match="secret_key must be set"):
            Settings(environment="production", secret_key="change-me-in-production")

    def test_explicit_secret_is_kept(self) -> None:
        s = Settings(environment="production", secret_key="prod-secret-32-chars-long!!!")
        assert s.secret_key == "prod-secret-32-chars-long!!!"

    @pytest.mark.parametrize("environment", ["development", "test", "staging"])
    def test_empty_secret_replaced_outside_production(
        self, environment: str, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.delenv("SECRET_KEY", raising=False)
        s = Settings(environment=environment, secret_key="")
        assert len(s.secret_key) >= 32
        assert s.secret_key != ""

    def test_generated_secrets_differ_between_instances(self) -> None:
        assert Settings(environment="test").secret_key != Settings(environment="test").secret_key

    def test_placeholder_replaced_outside_production(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("SECRET_KEY", raising=False)
        s = Settings(environment="development", secret_key="change-me-in-production")
        assert s.secret_key != "change-me-in-production"


@pytest.mark.unit
class TestSettingsSources:
    def test_env_vars_override_defaults(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("SECRET_KEY", "from-env-var-secret-32-chars!!!")
        monkeypatch.setenv("ENVIRONMENT", "test")
        monkeypatch.setenv("DATABASE_URL", "sqlite+aiosqlite:///./cfg_test.db")
        s = Settings()
        assert s.secret_key == "from-env-var-secret-32-chars!!!"
        assert s.environment == "test"
        assert s.database_url == "sqlite+aiosqlite:///./cfg_test.db"

    def test_defaults(self, monkeypatch: pytest.MonkeyPatch) -> None:
        for var in ("SECRET_KEY", "ENVIRONMENT", "DATABASE_URL", "REDIS_URL", "KAFKA_BOOTSTRAP"):
            monkeypatch.delenv(var, raising=False)
        s = Settings()
        assert s.environment == "development"
        assert s.access_token_expire_minutes == 30
        assert s.redis_url == "redis://localhost:6379/0"
        assert s.kafka_bootstrap == "localhost:9092"
