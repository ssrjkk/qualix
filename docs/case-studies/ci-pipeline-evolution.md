# CI Pipeline Evolution: From Red to Green

## Context

This case study documents the process of diagnosing and fixing a failing CI pipeline
for **qa-sentinel** — a full-stack QA automation platform with 7 testing layers
(unit, API, integration, external, contract, E2E, load).

The E2E tests were consistently failing in CI despite passing locally,
causing a 2-week debugging effort.

## Problem: Phantom Failures

The E2E test suite had 15 tests. In CI run #49, all 15 were red.
Key symptoms:
- 14/15 failures were `Locator.fill()` timeouts (30s)
- 1 failure was `wait_for_url` timeout
- All timestamps showed exactly 30s elapsed
- Locally (Playwright headed mode) all tests passed
- CI artifacts showed the login page rendered, but input fields were invisible

## Investigation

### Step 1: Chromium launch misconfiguration

The `pytest_collection_modifyitems` hook in conftest.py was launching a browser
during test collection (not just during test execution). This caused leaked
browser processes and unpredictable state.

**Fix:** Replaced browser launch with `import playwright` check.

### Step 2: Allure results corruption

Allure Docker service (running alongside tests) was consuming raw JSON result
files from `./allure-results` (mounted as root:755). The CI `runner` user
couldn't write to the directory. Additionally, the service polled for new files
and moved them, leaving the directory empty for the upload step.

**Fix:** Added `--scale allure=0` to Docker Compose start, excluding the service
from CI while preserving local dev behavior.

### Step 3: YAML indent bug

The "Report failed tests" step used a raw Python script indented under `run: |`.
A missing indentation level caused GitHub Actions to parse it as a separate
mapping key, making the workflow fall back to `filename-only` naming with 0 jobs.

**Fix:** Corrected YAML indentation (commit bdc1249).

### Step 4: Root Cause — sessionStorage leak

After all the above fixes, the E2E tests were still failing. The root cause was
a **sessionStorage leak** between tests:

1. `test_successful_login_redirects_to_dashboard` logs in, which stores an
   auth token in `sessionStorage`
2. Subsequent tests load the SPA and find the cached token
3. The SPA calls `showDashboard()` which hides `#login-view` with `display: none`
4. Input elements become invisible → `Locator.fill()` timeouts

Playwright reuses the same `BrowserContext` across tests in the same module,
so sessionStorage persists.

**Fix:** Added an autouse fixture `_clear_auth_state` that calls
`add_init_script("sessionStorage.clear()")` before every navigation,
preventing any stale token from being found.

## Postmortem

### What went well
- CI artifacts (screenshots, trace files) were critical for diagnosis
- The Allure report showed exactly which elements were timing out
- Local vs CI comparison narrowed the issue

### What we would do differently
- Add `new_context()` per test instead of sharing context
- Add explicit sessionStorage assertions in E2E tests
- Add a CI step to dump `sessionStorage` state for debugging

### Metrics

| Metric | Before | After |
|--------|--------|-------|
| E2E pass rate | 0/15 (0%) | 15/15 (100%) |
| CI run time | ~8 min | ~4 min |
| Failed steps per run | 3-4 | 0 |
| Allure results size | 0 B | 63 KB |

## Key Technical Details

### PushState Routing Issue

The SPA uses `history.pushState({}, '', '/dashboard')` which changes the URL
without triggering a page navigation. Playwright's `wait_for_url()` /
`expect_navigation()` never fire because no navigation event occurs.

**Solution:** Use `page.wait_for_function(() => window.location.href.includes('/dashboard'))`
instead of `expect(page).to_have_url()`.

### bcrypt 72-byte Limit

During property-based testing, Hypothesis discovered that `hash_password()`
raised `ValueError` for passwords longer than 72 bytes (bcrypt's internal limit).
This was a security vulnerability: an attacker could cause a 500 error or
truncation mismatch.

**Fix:** Added SHA-256 pre-hashing for passwords exceeding 72 bytes (OWASP
recommended approach).

## Tools Used

- pytest + Playwright (E2E)
- Allure (reporting)
- Hypothesis (property-based fuzzing)
- bcrypt (password hashing)
- GitHub Actions (CI)
