# Changelog

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
