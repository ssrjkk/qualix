.PHONY: help up down test test-unit test-integration test-api test-contract test-e2e test-load test-schemathesis cov lint fmt ci clean install setup pre-commit changelog security-scan serve-frontend schema test-external test-external-live test-kafka

help: ## Показать доступные команды
	@grep -E '^[a-zA-Z_-]+:.*?##' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

# ── Docker ────────────────────────────────────────────────────────────────────

up: ## Поднять все сервисы (postgres, redis, kafka, allure, grafana)
	docker compose up -d
	@echo "✓ app:     http://localhost:8080"
	@echo "✓ allure:  http://localhost:4040"
	@echo "✓ grafana: http://localhost:3000"

down: ## Остановить все сервисы
	docker compose down -v

# ── Тесты по слоям ───────────────────────────────────────────────────────────

test: ## Полный прогон (unit + integration + api + contract)
	mkdir -p reports
	python -m app.api.openapi > openapi.json
	pytest tests/unit/ tests/integration/ tests/api/ tests/contract/ \
		-q --no-header --alluredir=allure-results

test-unit: ## Unit тесты + coverage
	pytest tests/unit/ -m unit \
		--cov=app --cov-report=term-missing --cov-fail-under=80 -q

test-integration: ## Integration тесты (fakeredis + SQLite без Docker)
	pytest tests/integration/ -m integration -v --no-cov

test-api: ## API тесты
	mkdir -p reports
	python -m app.api.openapi > openapi.json
	pytest tests/api/ -m api -v --no-cov

test-contract: ## Contract тесты
	pytest tests/contract/ -m contract -v --no-cov

test-schemathesis: ## Schemathesis OpenAPI fuzzing
	mkdir -p reports
	python -m app.api.openapi > openapi.json
	pytest tests/api/test_schemathesis.py -v --no-cov

test-e2e: ## E2E тесты (нужен запущенный app: make up)
	E2E_TRACE=1 pytest tests/e2e/ -m e2e --no-cov --headed=false -n 4

test-load: ## Load тест (30s smoke, нужен make up)
	locust -f tests/load/locustfile.py --headless \
		-u 50 -r 10 -t 30s \
		--host http://localhost:8080 \
		--html reports/load-report.html
	@echo "✓ Load report: reports/load-report.html"

# ── Coverage ──────────────────────────────────────────────────────────────────

cov: ## Полный coverage report (html + xml)
	mkdir -p reports
	python -m app.api.openapi > openapi.json
	pytest tests/unit/ tests/api/ tests/contract/ \
		--cov=app \
		--cov-report=term-missing \
		--cov-report=html:reports/coverage-html \
		--cov-report=xml:reports/coverage.xml \
		--cov-fail-under=80 \
		-q --no-header
	@echo "✓ HTML: reports/coverage-html/index.html"
	@echo "✓ XML:  reports/coverage.xml"

cov-open: cov ## Coverage report + открыть в браузере
	open reports/coverage-html/index.html || xdg-open reports/coverage-html/index.html

# ── Качество кода ─────────────────────────────────────────────────────────────

lint: ## Ruff + mypy
	ruff check .
	ruff format --check .
	mypy app

fmt: ## Авто-форматирование
	ruff format .
	ruff check --fix .

# ── CI (локальный прогон как в GitHub Actions) ────────────────────────────────

test-external: ## External API тесты (respx моки — без сети)
	python -m app.api.openapi > openapi.json 2>/dev/null || true
	pytest tests/external/ -q --no-cov

test-external-live: ## External API тесты против реального dummyjson.com
	pytest tests/external/ --live-api -q --no-cov

test-kafka: ## Kafka integration тесты (in-memory)
	pytest tests/integration/test_kafka.py -v --no-cov

serve-frontend: ## Запустить приложение с фронтендом
	uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

ci: lint test-unit test-integration test-api test-contract test-external ## Полный CI pipeline локально

# ── Безопасность ──────────────────────────────────────────────────────────────

security-scan: ## SAST + dependency scan
	@echo "→ Bandit SAST scan..."
	@ruff check app --select S --quiet || true
	@echo "→ Safety dependency scan..."
	@pip install safety 2>/dev/null; safety check --full-report || true

# ── Dev Environment ───────────────────────────────────────────────────────────

install: ## Установить все зависимости + pre-commit
	uv pip install -e ".[test,load,lint]"
	playwright install chromium 2>/dev/null || true
	pip install pre-commit 2>/dev/null; pre-commit install --install-hooks 2>/dev/null || true
	@echo "✓ All dependencies installed"

pre-commit: ## Запустить pre-commit на всех файлах
	pre-commit run --all-files

setup: install pre-commit ## Полная настройка dev-окружения (install + pre-commit)

# ── Утилиты ───────────────────────────────────────────────────────────────────

clean: ## Удалить артефакты
	rm -rf allure-results allure-reports reports \
		.coverage coverage.xml *.db \
		**/__pycache__ **/*.pyc \
		.hypothesis pacts logs
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cleaned"

schema: ## Регенерировать openapi.json
	python -m app.api.openapi > openapi.json
	@echo "✓ openapi.json updated"

changelog: ## Сгенерировать CHANGELOG из git-cliff
	@pip install git-cliff 2>/dev/null; git-cliff --config .github/cliff.toml --output CHANGELOG.md
	@echo "✓ CHANGELOG.md regenerated"
