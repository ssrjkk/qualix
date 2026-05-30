"""Unit layer conftest — без IO, без фикстур из root."""

from __future__ import annotations

import pytest

from tests.factories.user_factory import PaymentRequestFactory, UserCreateFactory


@pytest.fixture
def valid_user():
    return UserCreateFactory()


@pytest.fixture
def user_weak_password():
    return UserCreateFactory(weak_password=True)


@pytest.fixture
def valid_payment():
    return PaymentRequestFactory()
