"""
pytest plugin — отслеживает flaky тесты и создаёт GitHub Issues.
"""
from __future__ import annotations
import json, os
from pathlib import Path
from collections import defaultdict
import pytest

FLAKY_LOG = Path("reports/flaky_tests.json")
_results: dict[str, list[str]] = defaultdict(list)


def pytest_runtest_logreport(report: pytest.TestReport) -> None:
    if report.when == "call":
        _results[report.nodeid].append(report.outcome)


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    flaky = [
        nid for nid, outcomes in _results.items()
        if "passed" in outcomes and "failed" in outcomes
    ]
    if not flaky:
        return
    FLAKY_LOG.parent.mkdir(exist_ok=True)
    FLAKY_LOG.write_text(json.dumps({"flaky_tests": flaky}, indent=2))
    print(f"\n⚠️  Flaky tests detected ({len(flaky)}):")
    for t in flaky:
        print(f"   - {t}")
    if os.environ.get("CREATE_GH_ISSUES") == "1":
        _create_issues(flaky)


def _create_issues(flaky_tests: list[str]) -> None:
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY", "ssrjkk/qa-sentinel")
    if not token:
        return
    import urllib.request, urllib.error
    for test in flaky_tests:
        body = json.dumps({
            "title": f"[Flaky] {test.split('::')[-1]}",
            "body": f"Flaky test detected.\n\nTest: `{test}`",
            "labels": ["flaky-test", "qa"],
        }).encode()
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/issues", data=body,
            headers={"Authorization": f"token {token}", "Content-Type": "application/json"},
        )
        try:
            urllib.request.urlopen(req)
        except urllib.error.URLError:
            pass
