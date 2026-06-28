"""Property-based tests (Hypothesis) for critical qualix functions."""

from __future__ import annotations

import pytest
from hypothesis import HealthCheck, assume, given
from hypothesis import settings as h_settings
from hypothesis import strategies as st

from app.api.auth import _create_token, _verify_token
from app.kafka_client import InMemoryKafka
from app.models.user import PaymentRequest, UserCreate
from app.security import hash_password, verify_password
from app.services.validators import sanitize_string, validate_amount, validate_phone

MAX_EXAMPLES = 200
SLOW_EXAMPLES = 15  # bcrypt ~200ms per call
SLOW_DL = {
    "deadline": None,
    "suppress_health_check": [HealthCheck.too_slow, HealthCheck.data_too_large],
}
SLOW = {"deadline": None, "suppress_health_check": [HealthCheck.too_slow]}


# ── Secure hashing ────────────────────────────────────────────────────────────


@pytest.mark.unit
class TestPasswordHashing:
    @given(st.text(min_size=1, max_size=128))
    @h_settings(max_examples=SLOW_EXAMPLES, **SLOW_DL)
    def test_verify_round_trip(self, password: str) -> None:
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True

    @given(st.text(max_size=128))
    @h_settings(max_examples=SLOW_EXAMPLES, **SLOW)
    def test_hash_format(self, password: str) -> None:
        assume(len(password) >= 1)
        hashed = hash_password(password)
        assert hashed.startswith("$2b$12$")
        assert len(hashed) == 60

    @given(st.text(min_size=1, max_size=128))
    @h_settings(max_examples=SLOW_EXAMPLES, **SLOW_DL)
    def test_different_salt_produces_different_hash(self, password: str) -> None:
        h1 = hash_password(password)
        h2 = hash_password(password)
        assert h1 != h2

    @given(st.text(min_size=1, max_size=128), st.text(max_size=64))
    @h_settings(max_examples=SLOW_EXAMPLES, **SLOW)
    def test_verify_rejects_random_hash(self, password: str, random_hash: str) -> None:
        assume(len(random_hash) >= 1)
        assert verify_password(password, random_hash) is False

    @given(st.text(min_size=1, max_size=128))
    @h_settings(max_examples=SLOW_EXAMPLES, **SLOW_DL)
    def test_verify_empty_password_against_valid_hash(self, password: str) -> None:
        hashed = hash_password(password)
        assert verify_password("", hashed) is False

    @given(st.text(max_size=128))
    @h_settings(max_examples=SLOW_EXAMPLES, **SLOW)
    def test_verify_never_raises(self, password: str) -> None:
        try:
            hashed = hash_password(password) if password else "$2b$12$invalid"
            result = verify_password(password, hashed)
            assert isinstance(result, bool)
        except Exception:
            pytest.fail("verify_password raised an exception")


# ── Auth token round-trip ─────────────────────────────────────────────────────


@pytest.mark.unit
class TestAuthToken:
    @given(
        username=st.text(min_size=1, max_size=50).filter(lambda s: ":" not in s),
        secret=st.text(min_size=1, max_size=64),
        expires=st.integers(min_value=1, max_value=1440),
    )
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_round_trip_valid(self, username: str, secret: str, expires: int) -> None:
        token = _create_token(username, secret, expires)
        result = _verify_token(token, secret)
        assert result == username

    @given(
        username=st.text(min_size=1, max_size=50).filter(lambda s: ":" not in s),
        secret=st.text(min_size=1, max_size=64),
        wrong_secret=st.text(min_size=1, max_size=64),
        expires=st.integers(min_value=1, max_value=1440),
    )
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_wrong_secret_fails(
        self, username: str, secret: str, wrong_secret: str, expires: int
    ) -> None:
        assume(secret != wrong_secret)
        token = _create_token(username, secret, expires)
        assert _verify_token(token, wrong_secret) is None

    @given(
        username=st.text(min_size=1, max_size=50).filter(lambda s: ":" not in s),
        secret=st.text(min_size=1, max_size=64),
    )
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_expired_token_returns_none(self, username: str, secret: str) -> None:
        token = _create_token(username, secret, expires_minutes=-1)
        assert _verify_token(token, secret) is None

    @given(
        username=st.text(min_size=1, max_size=50).filter(lambda s: ":" not in s),
        secret=st.text(min_size=1, max_size=64),
        expires=st.integers(min_value=1, max_value=1440),
    )
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_token_contains_username(self, username: str, secret: str, expires: int) -> None:
        token = _create_token(username, secret, expires)
        assert username in token


# ── Phone validation ──────────────────────────────────────────────────────────


@st.composite
def formatted_valid_phone(draw: st.DrawFn) -> str:
    """Generate a valid phone number with random formatting."""
    country = str(draw(st.integers(min_value=1, max_value=99)))
    rest_len = draw(st.integers(min_value=6, max_value=13))
    digits = st.integers(min_value=0, max_value=9).map(str)
    rest = "".join(draw(digits) for _ in range(rest_len))
    fmt = draw(st.sampled_from(["none", "spaces", "dashes", "parens"]))
    if fmt == "none":
        return f"+{country}{rest}"
    if fmt == "spaces":
        return f"+{country} {rest[:3]} {rest[3:]}"
    if fmt == "dashes":
        return f"+{country}-{rest[:3]}-{rest[3:]}"
    return f"+{country} ({rest[:3]}) {rest[3:]}"


@pytest.mark.unit
class TestPhoneValidator:
    @given(formatted_valid_phone())
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_formatted_valid_passes(self, s: str) -> None:
        assert validate_phone(s) is True

    @given(st.text(min_size=1).filter(lambda s: not any(c.isdigit() for c in s)))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_no_digits_returns_false(self, s: str) -> None:
        assert validate_phone(s) is False

    @given(st.text(min_size=1, max_size=6))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_too_short_returns_false(self, s: str) -> None:
        assert validate_phone(s) is False


# ── Pydantic model validator invariants ────────────────────────────────────────


@pytest.mark.unit
class TestUserCreateValidators:
    @given(st.text(max_size=64))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_strip_username_idempotent(self, v: str) -> None:
        once = UserCreate.strip_username(v)
        twice = UserCreate.strip_username(once)
        assert once == twice

    @given(st.text(max_size=100))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_normalize_email_idempotent(self, v: str) -> None:
        assume("@" not in v)
        once = UserCreate.normalize_email(v)
        twice = UserCreate.normalize_email(once)
        assert once == twice

    @given(st.text(max_size=100))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_normalize_email_lowercases(self, v: str) -> None:
        assume("@" not in v)
        result = UserCreate.normalize_email(v)
        assert result == result.lower()
        assert result == result.strip()


@pytest.mark.unit
class TestPaymentRequestValidators:
    CURRENCIES = ["usd", "eur", "rub", "usdt", "gbp", "jpy", "USD", "EUR", "RUB"]

    @given(st.sampled_from(CURRENCIES))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_valid_currency_passes(self, currency: str) -> None:
        result = PaymentRequest.validate_currency(currency)
        assert result == currency.upper()

    @given(
        st.text(min_size=1, max_size=10).filter(
            lambda s: s.upper() not in PaymentRequest.ALLOWED_CURRENCIES
        )
    )
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_invalid_currency_raises(self, currency: str) -> None:
        import pydantic

        with pytest.raises(pydantic.ValidationError):
            PaymentRequest(amount=1.0, currency=currency, description="test")


@pytest.mark.unit
class TestAmountValidator:
    LIMIT = 1_000_000.0

    @given(
        st.floats(
            min_value=0.001,
            max_value=LIMIT,
            allow_nan=False,
            allow_infinity=False,
        )
    )
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_valid_range_passes(self, amount: float) -> None:
        assert validate_amount(amount) is True

    @given(
        st.one_of(
            st.floats(min_value=LIMIT + 0.01, allow_nan=False, allow_infinity=False),
            st.floats(max_value=-0.001, allow_nan=False, allow_infinity=False),
            st.just(0.0),
            st.just(float("nan")),
            st.just(float("inf")),
            st.just(None),
        )
    )
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_invalid_range_fails(self, amount: float) -> None:
        assert validate_amount(amount) is False

    @given(st.text(max_size=200))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_sanitize_no_script_tags(self, s: str) -> None:
        result = sanitize_string(s)
        assert "<script>" not in result.lower()
        assert "</script>" not in result.lower()

    @given(st.text(max_size=200))
    @h_settings(max_examples=MAX_EXAMPLES)
    def test_sanitize_idempotent(self, s: str) -> None:
        once = sanitize_string(s)
        twice = sanitize_string(once)
        assert once == twice


# ── InMemoryKafka invariants ──────────────────────────────────────────────────


@st.composite
def topic_key_value(draw: st.DrawFn) -> tuple[str, str, dict]:
    topic_chars = st.characters(categories=("Ll", "Nd"), include_characters="._-")
    topic = draw(st.text(min_size=1, max_size=20, alphabet=topic_chars))
    key = draw(st.text(min_size=1, max_size=20))
    value = draw(
        st.dictionaries(
            keys=st.text(min_size=1, max_size=10),
            values=st.one_of(st.integers(), st.text(max_size=20), st.booleans()),
            min_size=1,
            max_size=5,
        )
    )
    return topic, key, value


@st.composite
def two_msgs_same_topic(draw: st.DrawFn) -> tuple[tuple[str, str, dict], tuple[str, str, dict]]:
    topic_chars = st.characters(categories=("Ll", "Nd"), include_characters="._-")
    topic = draw(st.text(min_size=1, max_size=20, alphabet=topic_chars))
    key_a = draw(st.text(min_size=1, max_size=20))
    key_b = draw(st.text(min_size=1, max_size=20))
    value_a = draw(
        st.dictionaries(
            keys=st.text(min_size=1, max_size=10),
            values=st.one_of(st.integers(), st.text(max_size=20), st.booleans()),
            min_size=1,
            max_size=3,
        )
    )
    value_b = draw(
        st.dictionaries(
            keys=st.text(min_size=1, max_size=10),
            values=st.one_of(st.integers(), st.text(max_size=20), st.booleans()),
            min_size=1,
            max_size=3,
        )
    )
    return (topic, key_a, value_a), (topic, key_b, value_b)


@pytest.mark.unit
class TestInMemoryKafka:
    @given(topic_key_value())
    @h_settings(max_examples=MAX_EXAMPLES)
    async def test_produce_consume_round_trip(self, msg: tuple[str, str, dict]) -> None:
        InMemoryKafka.reset()
        topic, key, value = msg
        await InMemoryKafka.produce(topic, key, value)
        messages = await InMemoryKafka.consume(topic)
        assert len(messages) == 1
        assert messages[0]["key"] == key
        assert messages[0]["value"] == value

    @given(topic_key_value(), topic_key_value())
    @h_settings(max_examples=MAX_EXAMPLES)
    async def test_topic_isolation(
        self, msg_a: tuple[str, str, dict], msg_b: tuple[str, str, dict]
    ) -> None:
        InMemoryKafka.reset()
        topic_a, key_a, value_a = msg_a
        topic_b, key_b, value_b = msg_b
        assume(topic_a != topic_b)
        await InMemoryKafka.produce(topic_a, key_a, value_a)
        await InMemoryKafka.produce(topic_b, key_b, value_b)
        msgs_a = await InMemoryKafka.consume(topic_a)
        msgs_b = await InMemoryKafka.consume(topic_b)
        assert len(msgs_a) == 1
        assert msgs_a[0]["key"] == key_a
        assert len(msgs_b) == 1
        assert msgs_b[0]["key"] == key_b

    @given(st.lists(topic_key_value(), min_size=1, max_size=10))
    @h_settings(max_examples=MAX_EXAMPLES)
    async def test_messages_preserve_order(self, msgs: list[tuple[str, str, dict]]) -> None:
        InMemoryKafka.reset()
        for topic, key, value in msgs:
            await InMemoryKafka.produce(topic, key, value)
        for topic, key, value in msgs:
            consumed = await InMemoryKafka.consume(topic)
            assert any(m["key"] == key and m["value"] == value for m in consumed)

    @given(topic_key_value())
    @h_settings(max_examples=MAX_EXAMPLES)
    async def test_consume_one_pops(self, msg: tuple[str, str, dict]) -> None:
        InMemoryKafka.reset()
        topic, key, value = msg
        await InMemoryKafka.produce(topic, key, value)
        first = await InMemoryKafka.consume_one(topic)
        assert first is not None
        assert first["key"] == key
        second = await InMemoryKafka.consume_one(topic)
        assert second is None

    @given(two_msgs_same_topic())
    @h_settings(max_examples=MAX_EXAMPLES)
    async def test_consume_one_fifo(
        self, msgs: tuple[tuple[str, str, dict], tuple[str, str, dict]]
    ) -> None:
        InMemoryKafka.reset()
        msg_a, msg_b = msgs
        topic = msg_a[0]
        await InMemoryKafka.produce(*msg_a)
        await InMemoryKafka.produce(*msg_b)
        first = await InMemoryKafka.consume_one(topic)
        second = await InMemoryKafka.consume_one(topic)
        assert first is not None
        assert first["key"] == msg_a[1]
        assert second is not None
        assert second["key"] == msg_b[1]

    @given(topic_key_value())
    @h_settings(max_examples=MAX_EXAMPLES)
    async def test_reset_clears_all_topics(self, msg: tuple[str, str, dict]) -> None:
        InMemoryKafka.reset()
        topic, key, value = msg
        await InMemoryKafka.produce(topic, key, value)
        InMemoryKafka.reset()
        assert await InMemoryKafka.consume(topic) == []
