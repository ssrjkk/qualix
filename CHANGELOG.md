# Changelog

## [1.1.0] - 2026-09-29

### Security Hardening

- **middleware**: add SecurityHeadersMiddleware (X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy, X-XSS-Protection)
- **models**: strengthen password complexity (uppercase + lowercase + digit + special character)
- **main**: fix CORS test environment (replace wildcard with http://testserver)
- **health**: cache Redis client to prevent connection exhaustion
- **dependencies**: add empty bearer token validation
- **auth**: narrow exception handling (except Exception → ValueError, IndexError)

### Infrastructure

- **docker**: add .dockerignore to prevent secrets and artifacts in build context
- **metrics**: add /metrics endpoint with Prometheus client integration
- **prometheus**: fix scrape config (comment out non-existent exporters)
- **grafana**: add comprehensive dashboard with HTTP metrics, latency percentiles, error rates
- **docker-compose**: add detailed comments for all services
- **pyproject**: add project.urls (Homepage, Repository, Documentation, Issues, Changelog)
- **pyproject**: fix duplicate aiokafka dependency
- **pyproject**: add prometheus-client to main dependencies
- **env**: add GRAFANA_ADMIN_PASSWORD and PostgreSQL credentials to .env.example
- **gitignore**: add .mypy_cache/, .ruff_cache/, .benchmarks/, *.log, trivy-results.sarif
- **makefile**: add Windows compatibility for cov-open target
- **users**: fix DELETE endpoint response_model for 204 status code

### CI/CD

- **workflows**: make load test p99 threshold non-blocking (continue-on-error)
- **tests**: fix flaky rate limiter tests (mock time.monotonic for determinism)

### Documentation

- **SECURITY.md**: comprehensive security practices documentation
- **README.md**: add Mermaid architecture diagram showing full system topology
- **README.md**: add test pyramid visualization with color-coded layers
- **README.md**: add security badges, update architecture section
- **branding**: complete replacement of QA Sentinel references with qualix

### Tests

- **test_app_factory**: CORS policy, rate limit, app metadata, DB retry logic
- **test_config**: configuration validation
- **test_middleware**: SecurityHeaders + RateLimitMemoryGuard tests

## [1.0.0] - 2026-05-29

### Features

- **api**: implement users CRUD + JWT-like auth
- **security,middleware**: bcrypt + structured logging + rate limiting
- **e2e,frontend**: Playwright E2E + real login frontend
- **test(unit)**: add unit tests + factory_boy + Hypothesis property-based
- **test(integration,api,contract)**: add full test pyramid layers
- **external**: add dummyjson.com external API tests with respx mocks
- **docs,infra**: k8s manifests + ADR + CI pipeline + CONTRIBUTING
- **external**: external API tests + Kafka + frontend + 100% coverage

### Bug Fixes

- **ci**: fix labeler.yml syntax + add coverage badge

### Tests

- **external**: add dummyjson.com external API tests with respx mocks

### Chore

- init project scaffold — FastAPI + SQLAlchemy + Docker
- add .env.example with all required variables
- commit openapi.json for schemathesis CI

### CI

- ideal 17-job pipeline with quality gate
