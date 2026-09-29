"""Unit тесты KafkaProducer — покрываем все ветки."""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from app.kafka_client import InMemoryKafka, KafkaProducer


@pytest.fixture(autouse=True)
def reset() -> None:
    InMemoryKafka.reset()
    yield
    InMemoryKafka.reset()


@pytest.mark.unit
class TestKafkaProducerBranches:
    async def test_start_mock_mode_returns_immediately(self) -> None:
        """mock-режим: start() не трогает брокер."""
        producer = KafkaProducer("localhost:9092", use_mock=True)
        await producer.start()  # должен вернуться без ошибок
        assert producer._mock is True

    async def test_start_real_mode_exception_fallback(self) -> None:
        """недоступный брокер → fallback на mock."""
        producer = KafkaProducer("localhost:9999", use_mock=False)
        # aiokafka.connect() упадёт → except → self._mock = True
        await producer.start()
        assert producer._mock is True  # переключился на mock

    async def test_stop_with_producer(self) -> None:
        """stop() отдаёт соединение внутреннему продюсеру."""
        producer = KafkaProducer("localhost:9092", use_mock=True)
        mock_inner = AsyncMock()
        producer._producer = mock_inner
        await producer.stop()
        mock_inner.stop.assert_awaited_once()

    async def test_stop_without_producer(self) -> None:
        """_producer отсутствует — stop() безопасен, ничего не вызвано."""
        producer = KafkaProducer("localhost:9092", use_mock=True)
        producer._producer = None
        await producer.stop()  # не падает

    async def test_send_non_mock_path(self) -> None:
        """не-мокированный путь идёт через _producer."""
        producer = KafkaProducer("localhost:9092", use_mock=False)
        producer._mock = False
        mock_inner = AsyncMock()
        producer._producer = mock_inner

        await producer.send("topic", "key", {"val": 1})

        mock_inner.send.assert_awaited_once_with("topic", key="key", value={"val": 1})

    async def test_consume_one_empty_returns_none(self) -> None:
        """consume_one на пустой топик → None."""
        result = await InMemoryKafka.consume_one("empty.topic")
        assert result is None


@pytest.mark.unit
class TestKafkaProducerMockEvents:
    async def test_send_in_mock_mode_lands_in_memory_queue(self) -> None:
        producer = KafkaProducer("localhost:9092", use_mock=True)
        await producer.start()

        await producer.send("user.events", "1", {"event": "ping"})

        assert await InMemoryKafka.consume("user.events") == [
            {"key": "1", "value": {"event": "ping"}}
        ]

    async def test_send_user_created_event(self) -> None:
        producer = KafkaProducer("localhost:9092", use_mock=True)

        await producer.send_user_created(7, "seven@t.com")

        (message,) = await InMemoryKafka.consume("user.events")
        assert message["key"] == "7"
        assert message["value"] == {
            "event": "user_created",
            "user_id": 7,
            "email": "seven@t.com",
        }

    async def test_send_user_deleted_event(self) -> None:
        producer = KafkaProducer("localhost:9092", use_mock=True)

        await producer.send_user_deleted(7)

        (message,) = await InMemoryKafka.consume("user.events")
        assert message["key"] == "7"
        assert message["value"] == {"event": "user_deleted", "user_id": 7}

    async def test_events_share_one_topic_in_order(self) -> None:
        producer = KafkaProducer("localhost:9092", use_mock=True)

        await producer.send_user_created(1, "one@t.com")
        await producer.send_user_deleted(1)

        events = [msg["value"]["event"] for msg in await InMemoryKafka.consume("user.events")]
        assert events == ["user_created", "user_deleted"]

    async def test_consume_one_pops_oldest_message(self) -> None:
        await InMemoryKafka.produce("user.events", "1", {"event": "first"})
        await InMemoryKafka.produce("user.events", "2", {"event": "second"})

        assert (await InMemoryKafka.consume_one("user.events"))["value"]["event"] == "first"
        assert (await InMemoryKafka.consume_one("user.events"))["value"]["event"] == "second"
        assert await InMemoryKafka.consume_one("user.events") is None
