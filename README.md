# QA Sentinel Platform

> Full-stack QA automation platform — Senior-level pet project 2026  
> **Ситников Сергей Алексеевич** · QA Automation Engineer Middle+

[![CI](https://github.com/ssrjkk/qa-sentinel/actions/workflows/ci.yml/badge.svg)](https://github.com/ssrjkk/qa-sentinel/actions)
[![Coverage](https://codecov.io/gh/ssrjkk/qa-sentinel/branch/main/graph/badge.svg)](https://codecov.io/gh/ssrjkk/qa-sentinel)
[![Python](https://img.shields.io/badge/python-3.12-blue)](https://python.org)
[![pytest](https://img.shields.io/badge/pytest-8.3-green)](https://pytest.org)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000)](https://github.com/astral-sh/ruff)

## Обзор

QA Sentinel — полноценная QA-платформа для мониторинга деградации API и UI.
Не просто набор тестов — отдельный продукт с архитектурой уровня Senior.

**Стек 2026:** Python 3.12 · pytest 8.3 · Playwright · Locust · FastAPI · SQLAlchemy · Docker · k8s · GitHub Actions · Allure · Prometheus · Grafana

## Быстрый старт

```bash
# 1. Клонируем
git clone git@github.com:ssrjkk/qa-sentinel.git && cd qa-sentinel

# 2. Зависимости
uv pip install -e ".[test,load,lint]"
playwright install chromium

# 3. Инфраструктура (опционально — без Docker тоже работает)
make up

# 4. Тесты
make test          # полный suite
make cov           # coverage report
```

## Структура проекта

```
qa-sentinel/
├── app/                          # FastAPI SUT (System Under Test)
│   ├── api/
│   │   ├── auth.py               # JWT-like auth, login endpoint
│   │   ├── users.py              # CRUD users
│   │   └── health.py             # /health (liveness) + /health/ready (readiness)
│   ├── models/
│   │   ├── db.py                 # SQLAlchemy ORM
│   │   └── user.py               # Pydantic schemas + validators
│   ├── repositories/
│   │   └── user_repo.py          # Data access layer
│   ├── services/
│   │   └── validators.py         # Pure business logic validators
│   ├── middleware.py             # RequestID · Logging · RateLimit
│   ├── security.py               # bcrypt password hashing
│   ├── logging_config.py         # structlog structured logging
│   ├── dependencies.py           # FastAPI DI: db, auth, settings
│   └── config.py                 # pydantic-settings
│
├── tests/
│   ├── conftest.py               # Session fixtures, Docker detection, SQLite fallback
│   ├── factories/
│   │   └── user_factory.py       # factory_boy: UserCreate, UserPayload, Payment
│   ├── unit/                     # Без IO — мгновенный запуск
│   │   ├── test_validators.py    # Email, phone, amount + Hypothesis 500 cases
│   │   ├── test_models.py        # Pydantic validation, normalization
│   │   ├── test_auth_internals.py # _create_token, _verify_token branches
│   │   ├── test_auth_router.py   # Auth router с AsyncMock
│   │   ├── test_users_router.py  # Users router с AsyncMock
│   │   ├── test_user_repo.py     # UserRepository с AsyncMock сессией
│   │   ├── test_dependencies.py  # get_settings, get_engine
│   │   ├── test_performance.py   # pytest-benchmark: bcrypt, token, validators
│   │   └── test_time_dependent.py # time-machine: token expiry
│   ├── integration/              # SQLite/Postgres + fakeredis
│   │   └── test_database.py      # UserRepository end-to-end + Redis ops
│   ├── api/                      # HTTP тесты через AsyncClient
│   │   ├── test_users_api.py     # CRUD + auth + pagination + edge cases
│   │   ├── test_auth_flows.py    # DB-path login, expired token, wrong secret
│   │   └── test_schemathesis.py  # OpenAPI fuzzing: schema validation + no-5xx
│   ├── contract/
│   │   └── test_api_contracts.py # JSON Schema контракты + security constraints
│   ├── e2e/                      # Playwright
│   │   ├── conftest.py           # Browser ctx, tracing, logged_in_page
│   │   ├── pages/                # Page Objects
│   │   └── test_auth_flow.py     # Login flow E2E
│   ├── load/
│   │   └── locustfile.py         # Locust + Prometheus metrics + p99 auto-stop
│   └── plugins/
│       └── flaky_tracker.py      # Авто-создание GitHub Issues для flaky тестов
│
├── infra/
│   ├── k8s/                      # Kubernetes манифесты
│   │   ├── namespace.yaml
│   │   ├── deployment.yaml       # RollingUpdate, liveness/readiness probes
│   │   ├── service.yaml
│   │   ├── hpa.yaml              # HPA: CPU/Memory autoscaling
│   │   └── secret.yaml           # Placeholder — use sealed-secrets в prod
│   ├── prometheus.yml            # Scrape: app + locust + postgres + redis
│   └── grafana/                  # Provisioning: datasource + dashboard
│
├── docs/adr/                     # Architecture Decision Records
│   ├── 001-custom-token-vs-jwt.md
│   ├── 002-sqlite-fallback-for-tests.md
│   ├── 003-bcrypt-for-passwords.md
│   ├── 004-fakeredis-in-tests.md
│   └── 005-json-schema-contracts-vs-pact.md
│
├── .github/workflows/ci.yml      # 8-stage CI: lint→unit→integration→api→contract→e2e→allure→badge
├── docker-compose.yml            # app + postgres + redis + kafka + allure + prometheus + grafana
├── Dockerfile
├── Makefile                      # 15 команд с документацией
├── pyproject.toml                # Все зависимости + coverage + ruff + mypy
└── CONTRIBUTING.md
```

## Тест-слои

| Слой | Файлы | Инструменты | Тестов | Coverage |
|------|-------|-------------|--------|----------|
| Unit | `tests/unit/` | pytest · Hypothesis · time-machine · benchmark | 122 | — |
| Integration | `tests/integration/` | testcontainers · fakeredis · SQLite | 17 | — |
| API | `tests/api/` | httpx · factory_boy · schemathesis | 48 | — |
| Contract | `tests/contract/` | JSON Schema contracts | 11 | — |
| E2E | `tests/e2e/` | Playwright POM · AI assertions · tracing | 7 | — |
| Load | `tests/load/` | Locust · Prometheus · p99 auto-stop | — | — |
| **Total** | | | **~205+** | **100%** |

## Ключевые фичи

### Тест-инфраструктура
- **factory_boy** — `UserCreateFactory`, `UserPayloadFactory` с traits (invalid_email, weak_password)
- **Hypothesis** — 500+ property-based cases для каждого валидатора
- **time-machine** — детерминированные тесты token expiry без зависимости от system clock
- **pytest-benchmark** — performance регрессии для bcrypt, token ops, Pydantic parsing
- **fakeredis** — Redis тесты без Docker (TTL, INCR, HSET, pub/sub)
- **Flaky tracker** — кастомный pytest plugin, авто-создание GitHub Issues
- **AI assertions** — `BasePage.ai_assert()` через Claude Sonnet для semantic UI checks

### Архитектура приложения
- **bcrypt rounds=12** — OWASP-compliant password hashing, constant-time verify
- **structlog** — structured JSON logging с request_id в каждом логе
- **RequestIDMiddleware** — `X-Request-ID` для distributed tracing
- **RateLimitMiddleware** — sliding window, 100 req/min per IP
- **`/health` + `/health/ready`** — liveness + readiness probes для k8s

### CI/CD
- **8-stage GitHub Actions** — lint → unit (+codecov) → integration → api → contract → e2e → allure → coverage-badge
- **Coverage enforcement** — `fail_under=80`, branch coverage, XML report
- **Zero-downtime deploy** — k8s RollingUpdate + `maxUnavailable=0`
- **HPA** — автомасштабирование по CPU/Memory (min=2, max=10)

## Команды

```bash
make help              # все доступные команды

# Тесты по слоям
make test-unit         # unit + coverage
make test-integration  # integration (fakeredis + SQLite)
make test-api          # API + schemathesis
make test-contract     # JSON Schema contracts
make test-e2e          # Playwright (нужен make up)
make test-load         # Locust 30s smoke

# Coverage
make cov               # term + html + xml
make cov-open          # открыть html в браузере

# Качество
make lint              # ruff + mypy
make fmt               # авто-форматирование

# CI
make ci                # lint + unit + integration + api + contract
make clean             # удалить артефакты
```

## ADR

Архитектурные решения задокументированы в [`docs/adr/`](docs/adr/):
- Почему custom token вместо JWT
- Почему SQLite fallback для тестов
- Почему bcrypt вместо SHA-256
- Почему fakeredis вместо mock
- Почему JSON Schema вместо Pact

## Автор

**Ситников Сергей Алексеевич**  
QA Automation Engineer (Middle+) · Saint Petersburg  
[GitHub](https://github.com/ssrjkk) · [Telegram](https://t.me/ssrjkk) · ray013lefe@gmail.com
