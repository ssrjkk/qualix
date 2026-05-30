"""Contract layer conftest."""

import pytest


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Пропускаем Pact тесты если pact-python не установлен."""
    skip = pytest.mark.skip(reason="pact-python not installed — pip install pact-python")
    for item in items:
        if "contract" in item.keywords and "pact" in item.name.lower():
            try:
                import pact  # noqa: F401
            except ImportError:
                item.add_marker(skip)
