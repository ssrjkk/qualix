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

- **bcrypt rounds=12** for password hashing (OWASP compliant)
- **Constant-time comparison** in token verification
- **No secrets in code** — use environment variables or sealed-secrets
- **Rate limiting** — 100 req/min per IP (sliding window)
- **Dependency scanning** via Dependabot (weekly) and CI (`safety check`)
- **SAST** via Bandit in CI pipeline
