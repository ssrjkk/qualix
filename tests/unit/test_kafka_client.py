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
        """line 53-54: if self._mock: return."""
        producer = KafkaProducer("localhost:9092", use_mock=True)
        await producer.start()  # должен вернуться без ошибок
        assert producer._mock is True

    async def test_start_real_mode_exception_fallback(self) -> None:
        """lines 55-64: real Kafka недоступен → fallback to mock."""
        producer = KafkaProducer("localhost:9999", use_mock=False)
        # aiokafka.connect() упадёт → except → self._mock = True
        await producer.start()
        assert producer._mock is True  # переключился на mock

    async def test_stop_with_producer(self) -> None:
        """lines 66-68: stop вызывает producer.stop()."""
        producer = KafkaProducer("localhost:9092", use_mock=True)
        mock_inner = AsyncMock()
        producer._producer = mock_inner
        await producer.stop()
        mock_inner.stop.assert_awaited_once()

    async def test_stop_without_producer(self) -> None:
        """line 67: if self._producer — None, stop не вызывается."""
        producer = KafkaProducer("localhost:9092", use_mock=True)
        producer._producer = None
        await producer.stop()  # не падает

    async def test_send_non_mock_path(self) -> None:
        """line 74: реальный send через _producer."""
        producer = KafkaProducer("localhost:9092", use_mock=False)
        producer._mock = False
        mock_inner = AsyncMock()
        producer._producer = mock_inner

        await producer.send("topic", "key", {"val": 1})

        mock_inner.send.assert_awaited_once_with("topic", key="key", value={"val": 1})

    async def test_consume_one_empty_returns_none(self) -> None:
        """line 38: consume_one на пустой топик → None."""
        result = await InMemoryKafka.consume_one("empty.topic")
        assert result is None
