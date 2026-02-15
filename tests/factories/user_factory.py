"""
factory_boy фабрики — единый источник тестовых данных для всего suite.
Используй вместо _user() / make_user_payload() везде.
"""
from __future__ import annotations

import factory
from faker import Faker

from app.models.user import UserCreate, PaymentRequest

fake = Faker("en_US")


class UserCreateFactory(factory.Factory):
    """Фабрика для Pydantic UserCreate."""

    class Meta:
        model = UserCreate

    username = factory.LazyFunction(lambda: fake.user_name()[:20])
    email = factory.LazyAttributeSequence(lambda o, n: f"{o.username}_{n}@example.com")
    password = "ValidPass1!"

    class Params:
        # Трейты — вариации фабрики
        weak_password = factory.Trait(password="weakpass")
        no_digits = factory.Trait(password="NoDigitsHere!")
        no_upper = factory.Trait(password="nouppercasehere1!")


class PaymentRequestFactory(factory.Factory):
    class Meta:
        model = PaymentRequest

    amount = factory.LazyFunction(lambda: round(fake.pyfloat(min_value=0.01, max_value=999_999, right_digits=2), 2))
    currency = factory.Iterator(["USD", "EUR", "RUB", "GBP"])
    description = factory.LazyFunction(lambda: fake.sentence(nb_words=4))


class UserPayloadFactory(factory.DictFactory):
    """
    Dict-фабрика для HTTP тестов.
    uuid.uuid4 — гарантированная уникальность между прогонами.
    """
    username = factory.LazyFunction(lambda: f"u_{__import__('uuid').uuid4().hex[:12]}")
    email = factory.LazyFunction(lambda: f"u_{__import__('uuid').uuid4().hex[:12]}@testmail.com")
    password = "ValidPass1!"

    class Params:
        invalid_email = factory.Trait(email="not-an-email")
        short_password = factory.Trait(password="Ab1!")
        no_upper = factory.Trait(password="nouppercasehere1!")
        no_digit = factory.Trait(password="NoDigitsHere!")
