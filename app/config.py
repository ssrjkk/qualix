import secrets

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://qa:qa@localhost:5432/qa_sentinel"
    redis_url: str = "redis://localhost:6379/0"
    kafka_bootstrap: str = "localhost:9092"
    environment: str = "development"
    secret_key: str = ""
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @field_validator("secret_key", mode="before")
    @classmethod
    def _reject_empty_secret(cls, v: str) -> str:
        if not v or v == "change-me-in-production":
            if __import__("os").environ.get("ENVIRONMENT") not in ("test", "development"):
                return secrets.token_urlsafe(32)
        return v
