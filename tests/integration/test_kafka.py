"""
Kafka integration тесты.

Три уровня:
1. InMemoryKafka — всегда работает, без зависимостей
2. testcontainers (Kafka) — если Docker доступен
3. Реальный Kafka — если KAFKA_BOOTSTRAP установлен

Паттерн тестирования: produce → consume → проверяем payload.
"""

from __future__ import annotations

import asyncio
import socket
import uuid

import pytest

from app.kafka_client import InMemoryKafka, KafkaProducer


def _kafka_available() -> bool:
    """Проверяем реальный Kafka на localhost:9092."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect(("127.0.0.1", 9092))
        s.close()
        return True
    except OSError:
        return False


KAFKA_UP = _kafka_available()


@pytest.fixture(autouse=True)
def reset_kafka() -> None:
    """Сбрасываем in-memory state перед каждым тестом."""
    InMemoryKafka.reset()
    yield
    InMemoryKafka.reset()


# ── InMemoryKafka тесты — всегда запускаются ─────────────────────────────────


@pytest.mark.integration
class TestInMemoryKafka:
    async def test_produce_and_consume(self) -> None:
        await InMemoryKafka.produce("test.topic", "key1", {"event": "test", "data": "hello"})
        messages = await InMemoryKafka.consume("test.topic")
        assert len(messages) == 1
        assert messages[0]["key"] == "key1"
        assert messages[0]["value"]["event"] == "test"

    async def test_multiple_messages_ordered(self) -> None:
        for i in range(5):
            await InMemoryKafka.produce("ordered.topic", f"key{i}", {"seq": i})
        messages = await InMemoryKafka.consume("ordered.topic")
        assert len(messages) == 5
        for i, msg in enumerate(messages):
            assert msg["value"]["seq"] == i

    async def test_consume_empty_topic_returns_empty(self) -> None:
        messages = await InMemoryKafka.consume("nonexistent.topic")
        assert messages == []

    async def test_consume_one_pops_message(self) -> None:
        await InMemoryKafka.produce("pop.topic", "k", {"val": 1})
        await InMemoryKafka.produce("pop.topic", "k", {"val": 2})

        first = await InMemoryKafka.consume_one("pop.topic")
        assert first is not None
        assert first["value"]["val"] == 1

        remaining = await InMemoryKafka.consume("pop.topic")
        assert len(remaining) == 1

    async def test_different_topics_isolated(self) -> None:
        await InMemoryKafka.produce("topic.a", "k", {"src": "a"})
        await InMemoryKafka.produce("topic.b", "k", {"src": "b"})

        msgs_a = await InMemoryKafka.consume("topic.a")
        msgs_b = await InMemoryKafka.consume("topic.b")

        assert msgs_a[0]["value"]["src"] == "a"
        assert msgs_b[0]["value"]["src"] == "b"

    async def test_reset_clears_all_topics(self) -> None:
        await InMemoryKafka.produce("topic.x", "k", {"x": 1})
        await InMemoryKafka.produce("topic.y", "k", {"y": 2})
        InMemoryKafka.reset()
        assert await InMemoryKafka.consume("topic.x") == []
        assert await InMemoryKafka.consume("topic.y") == []


# ── KafkaProducer с mock=True тесты ──────────────────────────────────────────


@pytest.mark.integration
class TestKafkaProducerMock:
    async def test_send_user_created_event(self) -> None:
        producer = KafkaProducer(bootstrap_servers="localhost:9092", use_mock=True)
        await producer.start()

        await producer.send_user_created(user_id=42, email="test@example.com")

        messages = await InMemoryKafka.consume("user.events")
        assert len(messages) == 1
        event = messages[0]["value"]
        assert event["event"] == "user_created"
        assert event["user_id"] == 42
        assert event["email"] == "test@example.com"
        assert messages[0]["key"] == "42"

    async def test_send_user_deleted_event(self) -> None:
        producer = KafkaProducer(bootstrap_servers="localhost:9092", use_mock=True)
        await producer.start()

        await producer.send_user_deleted(user_id=99)

        messages = await InMemoryKafka.consume("user.events")
        assert len(messages) == 1
        event = messages[0]["value"]
        assert event["event"] == "user_deleted"
        assert event["user_id"] == 99

    async def test_multiple_events_same_topic(self) -> None:
        producer = KafkaProducer(bootstrap_servers="localhost:9092", use_mock=True)
        await producer.start()

        await producer.send_user_created(1, "a@t.com")
        await producer.send_user_created(2, "b@t.com")
        await producer.send_user_deleted(1)

        messages = await InMemoryKafka.consume("user.events")
        assert len(messages) == 3
        events = [m["value"]["event"] for m in messages]
        assert events == ["user_created", "user_created", "user_deleted"]

    async def test_send_custom_event(self) -> None:
        producer = KafkaProducer(bootstrap_servers="localhost:9092", use_mock=True)
        await producer.start()

        uid = uuid.uuid4().hex
        await producer.send(
            topic="audit.events",
            key=uid,
            value={"action": "login", "user_id": 5, "ip": "127.0.0.1"},
        )

        messages = await InMemoryKafka.consume("audit.events")
        assert len(messages) == 1
        assert messages[0]["value"]["action"] == "login"
        assert messages[0]["key"] == uid

    async def test_event_order_guaranteed(self) -> None:
        """Kafka гарантирует порядок внутри одной partition (key)."""
        producer = KafkaProducer(bootstrap_servers="localhost:9092", use_mock=True)
        await producer.start()

        for i in range(10):
            await producer.send("order.topic", "same-key", {"seq": i})

        messages = await InMemoryKafka.consume("order.topic")
        seqs = [m["value"]["seq"] for m in messages]
        assert seqs == list(range(10))


# ── Сценарные тесты — user lifecycle events ───────────────────────────────────


@pytest.mark.integration
class TestUserLifecycleEvents:
    """
    Тестируем полный lifecycle пользователя через события.
    Create → Login → Delete → проверяем event log.
    """

    async def test_user_create_delete_event_sequence(self) -> None:
        producer = KafkaProducer(bootstrap_servers="localhost:9092", use_mock=True)
        await producer.start()

        user_id = 123
        email = "lifecycle@test.com"

        # Создаём пользователя
        await producer.send_user_created(user_id, email)

        # Дополнительные события
        await producer.send("audit.events", str(user_id), {"event": "login", "user_id": user_id})
        await producer.send(
            "audit.events", str(user_id), {"event": "profile_updated", "user_id": user_id}
        )

        # Удаляем
        await producer.send_user_deleted(user_id)

        # Проверяем user.events
        user_events = await InMemoryKafka.consume("user.events")
        assert len(user_events) == 2
        assert user_events[0]["value"]["event"] == "user_created"
        assert user_events[1]["value"]["event"] == "user_deleted"

        # Проверяем audit.events
        audit_events = await InMemoryKafka.consume("audit.events")
        assert len(audit_events) == 2

    async def test_concurrent_producers(self) -> None:
        """Несколько продюсеров пишут одновременно."""
        producers = [KafkaProducer("localhost:9092", use_mock=True) for _ in range(3)]
        for p in producers:
            await p.start()

        await asyncio.gather(
            *[p.send_user_created(i + 1, f"user{i}@t.com") for i, p in enumerate(producers)]
        )

        messages = await InMemoryKafka.consume("user.events")
        assert len(messages) == 3
        user_ids = {m["value"]["user_id"] for m in messages}
        assert user_ids == {1, 2, 3}


# ── Реальный Kafka (только если доступен) ────────────────────────────────────


@pytest.mark.integration
@pytest.mark.skipif(not KAFKA_UP, reason="Real Kafka not running (use make up)")
class TestRealKafka:
    async def test_real_kafka_produce_consume(self) -> None:
        import json

        from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

        topic = f"test.{uuid.uuid4().hex[:8]}"
        message = {"test": True, "id": uuid.uuid4().hex}

        # Produce
        producer = AIOKafkaProducer(
            bootstrap_servers="localhost:9092",
            value_serializer=lambda v: json.dumps(v).encode(),
        )
        await producer.start()
        await producer.send_and_wait(topic, message)
        await producer.stop()

        # Consume
        consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers="localhost:9092",
            auto_offset_reset="earliest",
            value_deserializer=lambda v: json.loads(v),
            consumer_timeout_ms=3000,
        )
        await consumer.start()
        received = []
        async for msg in consumer:
            received.append(msg.value)
            break
        await consumer.stop()

        assert len(received) == 1
        assert received[0]["test"] is True
