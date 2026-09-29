# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

This is a QA automation pet project, not a production service.
If you find a security issue:

1. **DO NOT** open a public GitHub Issue
2. Email: [ray013lefe@gmail.com](mailto:ray013lefe@gmail.com)
3. Expect acknowledgment within 72 hours

## Security Practices

### Authentication & Tokens
- **bcrypt rounds=12** for password hashing (OWASP compliant, SHA-256 pre-hash for >72 byte passwords)
- **HMAC-SHA256 tokens** with constant-time comparison (`hmac.compare_digest`)
- **Token expiry validation** with server-side UTC timestamp checks
- **Strong password policy** — uppercase + lowercase + digit + special character required

### Network & Headers
- **Security headers** on every response: `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`
- **CORS hardening** — per-environment origins (production: none, dev: localhost only, test: testserver only)
- **Rate limiting** — 100 req/min per IP (sliding window, in-memory with bounded dict)

### Input Validation
- **Pydantic schemas** enforce type constraints, email validation, username character restrictions
- **XSS sanitization** via `sanitize_string()` (strips `<script>` tags and HTML)
- **Decimal for money** — `PaymentRequest.amount` uses `Decimal`, not `float`
- **Parameterized SQL** — all queries via SQLAlchemy ORM, no raw string concatenation

### Infrastructure
- **No secrets in code** — use environment variables or sealed-secrets
- **Secret key validation** — production requires explicit `SECRET_KEY`
- **Dependency scanning** via Dependabot (weekly) and CI (`safety check`)
- **SAST** via Bandit in CI pipeline
- **Container scanning** via Trivy (CRITICAL/HIGH severity)
- **Secret scanning** enabled on GitHub
- **Kubernetes secrets** via `secretRef`, never in ConfigMaps

### Known Issues
- **NLTK GHSA-8mgp-746c-j5xp** (transitive dep via schemathesis) — no patched version on PyPI yet. Monitoring for 3.10.4+ release.
