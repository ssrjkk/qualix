"""Structured logging через structlog."""

from __future__ import annotations

import logging
import sys

import structlog


def configure_logging(environment: str = "development") -> None:
    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
    ]

    if environment == "production":
        processors = shared_processors + [structlog.processors.JSONRenderer()]
    else:
        processors = shared_processors + [structlog.dev.ConsoleRenderer(colors=False)]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG),
        context_class=dict,
        logger_factory=structlog.WriteLoggerFactory(sys.stdout),
        cache_logger_on_first_use=False,
    )


def get_logger(name: str) -> structlog.BoundLogger:  # type: ignore[type-arg]
    return structlog.get_logger(name)
