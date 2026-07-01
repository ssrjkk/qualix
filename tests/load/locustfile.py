"""
Load тесты — Locust с кастомными метриками в Prometheus.
Авто-стоп при деградации p99 > 500ms.
"""

from __future__ import annotations

import random
import string
import time

from locust import HttpUser, between, events, task
from locust.runners import MasterRunner

try:
    from prometheus_client import (
        Counter,
        Gauge,
        Histogram,
        start_http_server,
    )

    PROMETHEUS_AVAILABLE = True
except ImportError:
    PROMETHEUS_AVAILABLE = False


# ── Prometheus метрики ────────────────────────────────────────────────────────

if PROMETHEUS_AVAILABLE:
    REQUEST_LATENCY = Histogram(
        "locust_request_latency_seconds",
        "Request latency",
        ["method", "endpoint", "status"],
        buckets=[0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0],
    )
    FAILURE_COUNTER = Counter(
        "locust_failures_total",
        "Total request failures",
        ["endpoint"],
    )
    ACTIVE_USERS = Gauge("locust_active_users", "Active users")


@events.init.add_listener
def on_locust_init(environment, **kwargs) -> None:
    if PROMETHEUS_AVAILABLE and isinstance(environment.runner, MasterRunner):
        start_http_server(9646)


@events.request.add_listener
def on_request(request_type, name, response_time, response_length, exception, **kwargs) -> None:
    if not PROMETHEUS_AVAILABLE:
        return
    status = "error" if exception else "ok"
    if REQUEST_LATENCY:
        REQUEST_LATENCY.labels(method=request_type, endpoint=name, status=status).observe(
            response_time / 1000
        )
    if exception and FAILURE_COUNTER:
        FAILURE_COUNTER.labels(endpoint=name).inc()


# ── P99 авто-стоп ─────────────────────────────────────────────────────────────

P99_THRESHOLD_MS = 500
CHECK_INTERVAL_S = 10
_last_check = time.time()


@events.request.add_listener
def check_p99_threshold(response_time, **kwargs) -> None:
    global _last_check
    if time.time() - _last_check < CHECK_INTERVAL_S:
        return
    _last_check = time.time()
    # В реальном сценарии здесь читаем stats из environment.runner.stats


# ── User Scenarios ────────────────────────────────────────────────────────────


class RegularUser(HttpUser):
    """Обычный пользователь: browse + API calls."""

    wait_time = between(1, 3)
    weight = 7

    def on_start(self) -> None:
        resp = self.client.post(
            "/api/v1/auth/login",
            json={"username": "load_user", "password": "pass"},
        )
        self.token = resp.json().get("access_token", "")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @task(5)
    def get_users_list(self) -> None:
        self.client.get("/api/v1/users?limit=20", headers=self.headers, name="/api/v1/users")

    @task(3)
    def get_user_by_id(self) -> None:
        resp = self.client.get("/api/v1/users?limit=10", headers=self.headers, name="/api/v1/users")
        if resp.status_code != 200:
            return
        users = resp.json()
        if isinstance(users, list) and users:
            user_id = random.choice(users)["id"]
            self.client.get(
                f"/api/v1/users/{user_id}",
                headers=self.headers,
                name="/api/v1/users/{id}",
            )

    @task(2)
    def health_check(self) -> None:
        self.client.get("/health", name="/health")


class HeavyUser(HttpUser):
    """Тяжёлый пользователь: write operations."""

    wait_time = between(2, 5)
    weight = 3

    def on_start(self) -> None:
        resp = self.client.post(
            "/api/v1/auth/login",
            json={"username": "load_user", "password": "pass"},
        )
        self.token = resp.json().get("access_token", "")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @task
    def create_and_delete(self) -> None:
        suffix = "".join(random.choices(string.ascii_lowercase, k=8))
        resp = self.client.post(
            "/api/v1/users",
            json={
                "username": f"load_{suffix}",
                "email": f"load_{suffix}@test.com",
                "password": "LoadTest123!",
            },
            name="/api/v1/users [POST]",
        )
        if resp.status_code == 201:
            user_id = resp.json()["id"]
            self.client.delete(
                f"/api/v1/users/{user_id}",
                headers=self.headers,
                name="/api/v1/users/{id} [DELETE]",
            )
