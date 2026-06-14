from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import schemathesis
from httpx import AsyncClient

SCHEMA_PATH = Path(__file__).parent.parent.parent / "openapi.json"


@pytest.mark.api
def test_openapi_schema_structure() -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    assert schema.get("openapi", "").startswith("3.")
    assert "paths" in schema
    assert "info" in schema
    assert schema["info"]["title"] == "QA Sentinel"


@pytest.mark.api
def test_openapi_all_endpoints_present() -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    paths = schema["paths"]
    required = {"/health", "/api/v1/users", "/api/v1/users/{user_id}", "/api/v1/auth/login"}
    missing = required - set(paths.keys())
    assert not missing, f"Missing endpoints in OpenAPI schema: {missing}"


@pytest.mark.api
def test_openapi_endpoints_have_responses() -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    for path, methods in schema["paths"].items():
        for method, spec in methods.items():
            if method == "parameters":
                continue
            assert "responses" in spec, f"{method.upper()} {path} missing 'responses'"
            assert len(spec["responses"]) > 0, f"{method.upper()} {path} has empty 'responses'"


@pytest.mark.api
def test_openapi_post_endpoints_have_request_body() -> None:
    schema = json.loads(SCHEMA_PATH.read_text())
    for path, methods in schema["paths"].items():
        if "post" in methods:
            spec = methods["post"]
            assert "requestBody" in spec, f"POST {path} missing 'requestBody' in OpenAPI schema"


@pytest.mark.api
def test_schemathesis_loads_all_operations() -> None:
    schema = schemathesis.openapi.from_path(str(SCHEMA_PATH))
    ops = [r.ok() for r in schema.get_all_operations()]
    assert len(ops) >= 6, f"Expected >=6 operations, got {len(ops)}"
    methods_paths = {(o.method.upper(), o.path) for o in ops}
    assert any(path.startswith("/health") for _, path in methods_paths)
    assert ("POST", "/api/v1/users") in methods_paths
    assert ("GET", "/api/v1/users") in methods_paths
    assert ("DELETE", "/api/v1/users/{user_id}") in methods_paths


@pytest.mark.api
@pytest.mark.slow
async def test_schemathesis_no_5xx(client: AsyncClient) -> None:
    schema = schemathesis.openapi.from_path(str(SCHEMA_PATH))
    ops = [r.ok() for r in schema.get_all_operations()]

    for op in ops:
        test_cases = _build_test_cases(op)
        for method, url, kwargs in test_cases:
            resp = await getattr(client, method)(url, **kwargs)
            assert resp.status_code < 500, (
                f"5xx SERVER ERROR\n"
                f"  Operation: {method.upper()} {op.path}\n"
                f"  URL: {url}\n"
                f"  Status: {resp.status_code}\n"
                f"  Body: {resp.text[:400]}"
            )


def _build_test_cases(op: Any) -> list[tuple[str, str, dict]]:
    import uuid

    method = op.method.lower()
    path = op.path

    if "{user_id}" in path:
        path_cases = [
            path.replace("{user_id}", "1"),
            path.replace("{user_id}", "999999"),
            path.replace("{user_id}", "0"),
        ]
    else:
        path_cases = [path]

    cases = []
    for url in path_cases:
        kwargs: dict = {}

        if method == "post" and "auth" in url:
            kwargs["json"] = {"username": "test_user", "password": "test_pass"}
        elif method == "post" and "users" in url:
            uid = uuid.uuid4().hex[:8]
            kwargs["json"] = {
                "username": f"fuzz_{uid}",
                "email": f"fuzz_{uid}@test.com",
                "password": "FuzzPass1!",
            }

        if url != "/health" and method != "post":
            kwargs["headers"] = {"Authorization": "Bearer fake.token.for.fuzz"}

        cases.append((method, url, kwargs))

    return cases


@pytest.mark.api
@pytest.mark.slow
async def test_schemathesis_invalid_inputs_no_500(client: AsyncClient) -> None:
    invalid_inputs = [
        ("post", "/api/v1/users", {"json": {}}),
        ("post", "/api/v1/users", {"json": {"username": "x", "email": "bad", "password": "x"}}),
        ("post", "/api/v1/users", {"json": None}),
        ("post", "/api/v1/auth/login", {"json": {}}),
        ("post", "/api/v1/auth/login", {"json": {"username": "", "password": ""}}),
        ("get", "/api/v1/users/not_a_number", {}),
        ("get", "/api/v1/users/-1", {}),
        ("delete", "/api/v1/users/not_a_number", {}),
    ]

    for method, url, kwargs in invalid_inputs:
        resp = await getattr(client, method)(url, **kwargs)
        assert resp.status_code != 500, (
            f"5xx on invalid input: {method.upper()} {url}\n"
            f"Input: {kwargs}\n"
            f"Response: {resp.text[:300]}"
        )
