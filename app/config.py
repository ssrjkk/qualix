import secrets

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://qa:qa@localhost:5432/qualix"
    redis_url: str = "redis://localhost:6379/0"
    kafka_bootstrap: str = "localhost:9092"
    environment: str = "development"
    secret_key: str = ""
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @model_validator(mode="after")
    def _ensure_secret_key(self) -> "Settings":
        if self.secret_key not in ("", "change-me-in-production"):
            return self
        if self.environment == "production":
            # Случайный ключ в production ломает валидацию токенов между
            # репликами и после рестарта — конфигурацию видно сразу.
            raise ValueError("secret_key must be set in production environment")
        self.secret_key = secrets.token_urlsafe(32)
        return self
