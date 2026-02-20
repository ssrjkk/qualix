"""Integration layer conftest."""
from __future__ import annotations

import pytest
from tests.factories.user_factory import UserCreateFactory


@pytest.fixture
def user_data():
    return UserCreateFactory()


@pytest.fixture
def batch_user_data():
    return UserCreateFactory.build_batch(15)
