"""Unit тесты фабрики приложения: CORS, rate limit и ретраи БД при старте."""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import asynccontextmanager

import pytest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import Settings
from app.main import create_app
from app.middleware import RateLimitMiddleware

PROD_SECRET = "unit-test-secret-key-32chars!!"


@pytest.fixture
def restore_dependencies() -> Iterator[None]:
    """create_app() подменяет глобалы app.dependencies — снимаем и возвращаем снимок."""
    import app.dependencies as deps

    snapshot = (deps._test_settings, deps._shared_engine, deps._session_factory)
    try:
        yield
    finally:
        deps._test_settings, deps._shared_engine, deps._session_factory = snapshot


def _middleware_kwargs(application: FastAPI, cls: type) -> dict:
    for mw in application.user_middleware:
        if mw.cls is cls:
            return mw.kwargs
    raise AssertionError(f"{cls.__name__} is not installed")


@pytest.mark.unit
class TestCORSPolicy:
    @pytest.mark.parametrize(
        ("environment", "expected_origins"),
        [
            ("production", []),
            ("staging", []),
            ("development", ["http://localhost:3000", "http://localhost:5173"]),
            ("test", ["http://testserver"]),
        ],
    )
    def test_allow_origins_by_environment(
        self, restore_dependencies: None, environment: str, expected_origins: list[str]
    ) -> None:
        application = create_app(Settings(environment=environment, secret_key=PROD_SECRET))
        kwargs = _middleware_kwargs(application, CORSMiddleware)
        assert kwargs["allow_origins"] == expected_origins

    @pytest.mark.parametrize("environment", ["production", "staging"])
    def test_public_environments_never_wildcard(
        self, restore_dependencies: None, environment: str
    ) -> None:
        application = create_app(Settings(environment=environment, secret_key=PROD_SECRET))
        kwargs = _middleware_kwargs(application, CORSMiddleware)
        assert "*" not in kwargs["allow_origins"]
        assert kwargs["allow_credentials"] is True


@pytest.mark.unit
class TestRateLimitByEnvironment:
    @pytest.mark.parametrize(
        ("environment", "expected_limit"),
        [("test", 10000), ("development", 100), ("production", 100)],
    )
    def test_limit_by_environment(
        self, restore_dependencies: None, environment: str, expected_limit: int
    ) -> None:
        application = create_app(Settings(environment=environment, secret_key=PROD_SECRET))
        kwargs = _middleware_kwargs(application, RateLimitMiddleware)
        assert kwargs["limit"] == expected_limit
        assert kwargs["window"] == 60.0


@pytest.mark.unit
class TestAppMetadata:
    def test_title_and_version(self, restore_dependencies: None) -> None:
        application = create_app(Settings(environment="test", secret_key=PROD_SECRET))
        assert application.title == "qualix"
        assert application.version == "1.0.0"


class _FakeConn:
    async def run_sync(self, fn: object) -> None:
        return None


class _FlakyEngine:
    """Двигатель, отказывающий первые `fail_times` попыток begin()."""

    def __init__(self, fail_times: int) -> None:
        self._fail_times = fail_times
        self.attempts = 0
        self.opened = 0

    @asynccontextmanager
    async def begin(self):
        self.attempts += 1
        if self.attempts <= self._fail_times:
            raise OSError("connection refused")
        self.opened += 1
        yield _FakeConn()


def _app_with(environment: str = "test") -> FastAPI:
    application = FastAPI()
    application.state.settings = Settings(environment=environment, secret_key=PROD_SECRET)
    return application


@pytest.mark.unit
class TestLifespanDBRetry:
    async def test_startup_retries_until_db_answers(self, monkeypatch: pytest.MonkeyPatch) -> None:
        import asyncio

        import app.dependencies as deps
        import app.main as main_module

        waits: list[float] = []

        async def fake_sleep(delay: float) -> None:
            waits.append(delay)

        monkeypatch.setattr(asyncio, "sleep", fake_sleep)
        engine = _FlakyEngine(fail_times=2)
        monkeypatch.setattr(deps, "get_engine", lambda settings: engine)

        async with main_module.lifespan(_app_with()):
            pass

        # 2 отказа → 2 паузы по экспоненте, третья попытка успешна
        assert waits == [2, 4]
        assert (engine.attempts, engine.opened) == (3, 1)

    async def test_startup_fails_after_max_retries(self, monkeypatch: pytest.MonkeyPatch) -> None:
        import asyncio

        import app.dependencies as deps
        import app.main as main_module

        async def fake_sleep(delay: float) -> None:
            return None

        monkeypatch.setattr(asyncio, "sleep", fake_sleep)
        engine = _FlakyEngine(fail_times=10_000)
        monkeypatch.setattr(deps, "get_engine", lambda settings: engine)

        with pytest.raises(RuntimeError, match="Database unavailable after retries") as exc:
            async with main_module.lifespan(_app_with()):
                pass

        assert engine.attempts == 10
        assert isinstance(exc.value.__cause__, OSError)
