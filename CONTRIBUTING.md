# Contributing to QA Sentinel

## Быстрый старт

```bash
git clone git@github.com:ssrjkk/qa-sentinel.git
cd qa-sentinel
uv pip install -e ".[test,load,lint]"
playwright install chromium
make up        # поднять инфраструктуру
make test      # запустить все тесты
```

## Структура тестов

```
tests/
├── unit/         # Без IO. Запуск: make test-unit
├── integration/  # SQLite/Postgres + fakeredis. Запуск: make test-integration  
├── api/          # HTTP через AsyncClient. Запуск: make test-api
├── contract/     # JSON Schema контракты. Запуск: make test-contract
├── e2e/          # Playwright браузер. Запуск: make test-e2e
└── load/         # Locust. Запуск: make test-load
```

## Правила написания тестов

### Именование
```
test_<что>_<условие>_<ожидаемый результат>
test_create_user_duplicate_email_returns_409
test_verify_token_expired_returns_none
```

### Маркеры (обязательно)
```python
@pytest.mark.unit        # нет IO
@pytest.mark.api         # HTTP тесты
@pytest.mark.integration # реальные зависимости
@pytest.mark.contract    # контракты
@pytest.mark.e2e         # браузер
@pytest.mark.slow        # > 10s
```

### Фабрики вместо хардкода
```python
# ❌ Плохо
payload = {"username": "user1", "email": "user1@test.com", "password": "Pass1!"}

# ✅ Хорошо  
from tests.factories.user_factory import UserPayloadFactory
payload = UserPayloadFactory()
```

### Изоляция
- Unit тесты: `AsyncMock` для всех зависимостей
- Integration тесты: `db_session` фикстура с rollback
- API тесты: UUID в данных — нет конфликтов между прогонами

## Coverage

Минимум: **80%** (enforced в CI).  
Цель: **100%** (текущее состояние).

```bash
make cov        # полный report
make cov-open   # открыть в браузере
```

## Performance тесты

```bash
# Запуск с benchmark отчётом
pytest tests/unit/test_performance.py --benchmark-only --benchmark-sort=mean

# Сравнение с baseline
pytest tests/unit/test_performance.py --benchmark-compare
```

## Коммит-конвенция

```
feat(api): add cursor-based pagination
fix(auth): verify token with constant-time comparison
test(unit): add benchmark for bcrypt hashing
refactor(repo): extract base repository class
docs(adr): document JWT vs custom token decision
```

## PR checklist

- [ ] Тесты написаны для нового кода
- [ ] `make lint` проходит без ошибок
- [ ] `make test` 100% pass
- [ ] Coverage не упала ниже 80%
- [ ] Добавлен/обновлён ADR если принято архитектурное решение
