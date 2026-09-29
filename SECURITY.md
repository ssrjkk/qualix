# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue in qualix, please help us responsibly disclose it.

### How to Report

**Option 1: GitHub Security Advisories (Preferred)**
1. Go to [Security Advisories](https://github.com/ssrjkk/qualix/security/advisories)
2. Click "Report a vulnerability"
3. Fill out the form with details about the vulnerability

**Option 2: Email**
- Email: ray013lefe@gmail.com
- Include "[SECURITY]" in the subject line
- Provide detailed description and reproduction steps

### What to Include

- Description of the vulnerability
- Steps to reproduce or proof-of-concept
- Potential impact
- Suggested fix (if any)
- CVSS score (if known)

### Response Timeline

- **Initial response**: Within 48 hours
- **Status update**: Every 5 business days
- **Resolution target**: 30 days for critical/high severity

### Disclosure Policy

- We follow **coordinated disclosure**
- Please do not disclose the vulnerability publicly until we've had a chance to address it
- We will credit reporters in our security advisories (unless you prefer to remain anonymous)
- We will publish a CVE if appropriate

## Security Measures

qualix implements multiple layers of security:

### Authentication & Authorization
- **HMAC-SHA256 tokens** with constant-time verification (timing attack resistant)
- **bcrypt password hashing** (rounds=12, OWASP compliant)
- **Strict password policy**: uppercase + lowercase + digit + special character required
- **Empty token rejection** prevents null/empty bypass attacks

### Network Security
- **Security headers** on every response:
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `Permissions-Policy: geolocation=(), camera=(), microphone=()`
  - `X-XSS-Protection: 0` (modern browsers use CSP instead)
- **CORS hardening**: per-environment origins (production: no origins, development: localhost only)
- **Rate limiting**: 100 req/min per IP, sliding window, bounded memory (prevents DoS)
- **Request ID tracking**: `X-Request-ID` for distributed tracing and audit logs

### Data Protection
- **No secrets in code**: all sensitive data via environment variables
- **Kubernetes sealed-secrets**: encrypted secrets in GitOps workflow
- **Decimal for money**: `PaymentRequest.amount` uses `Decimal`, not `float` (prevents precision errors)
- **Input validation**: Pydantic validators with strict type checking
- **SQL injection prevention**: SQLAlchemy ORM with parameterized queries

### Infrastructure
- **Bandit SAST**: static analysis in CI pipeline
- **Safety dependency scan**: checks for known vulnerable dependencies
- **Trivy container scanning**: Docker image vulnerability detection
- **Dependabot**: weekly automated dependency updates
- **pre-commit hooks**: bandit SAST + detect-private-key before every commit

### Testing
- **Contract tests**: JSON Schema validation ensures API contracts
- **Schemathesis fuzzing**: OpenAPI property-based testing catches edge cases
- **Security-focused unit tests**: token expiry, password complexity, CORS validation
- **100% code coverage**: all code paths tested

## Security Best Practices for Deployment

When deploying qualix to production:

1. **Change default secrets**
   ```bash
   # Generate a strong secret key
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

2. **Use PostgreSQL** (not SQLite)
   ```bash
   DATABASE_URL=postgresql+asyncpg://user:strong-password@host:5432/qualix
   ```

3. **Enable TLS/SSL**
   - Use a reverse proxy (nginx, Traefik) with Let's Encrypt
   - Set `ENVIRONMENT=production` to disable CORS

4. **Kubernetes secrets**
   - Use sealed-secrets or external secret managers (Vault, AWS Secrets Manager)
   - Never commit real secrets to Git

5. **Rate limiting**
   - Adjust `RateLimitMiddleware` based on your traffic patterns
   - Consider using an API gateway (Kong, Envoy) for production

6. **Monitoring**
   - Enable Prometheus + Grafana for observability
   - Set up alerts for rate limit violations and authentication failures
   - Monitor for unusual patterns in structured logs

7. **Regular updates**
   - Keep dependencies updated (`dependabot` is configured)
   - Run `safety check` regularly
   - Review Dependabot alerts weekly

## Known Security Limitations

- **NLTK transitive dependency**: schemathesis depends on nltk, which has a known vulnerability (GHSA-8mgp-746c-j5xp). No patched version available. Vulnerable code paths are not used in qualix. Tracked in [Issue #42](https://github.com/ssrjkk/qualix/issues/42).

## Security Audit History

- **2026-09-29**: Initial security hardening (v1.1.0)
  - Added SecurityHeadersMiddleware
  - Strengthened password complexity
  - Fixed CORS test environment
  - Cached Redis client to prevent connection exhaustion
  - Added empty bearer token validation
  - Narrowed exception handling in auth

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [FastAPI Security Documentation](https://fastapi.tiangolo.com/tutorial/security/)
- [bcrypt Documentation](https://github.com/pyca/bcrypt)
- [Python Security Best Practices](https://docs.python.org/3/library/security.html)

## Contact

- **Security issues**: ray013lefe@gmail.com
- **General questions**: [GitHub Discussions](https://github.com/ssrjkk/qualix/discussions)
- **Telegram**: [@ssrjkk](https://t.me/ssrjkk)
