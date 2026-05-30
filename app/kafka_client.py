"""
Kafka client — publish/consume events.
В тестах: используется fakeredis-подобный подход — in-memory очередь
без реального Kafka брокера.
"""

from __future__ import annotations

import json
from collections import defaultdict
from typing import Any


class InMemoryKafka:
    """
    Лёгкий in-memory Kafka для тестов.
    Реальный Kafka (aiokafka) используется в production.
    """

    _topics: dict[str, list[dict]] = defaultdict(list)

    @classmethod
    def reset(cls) -> None:
        cls._topics.clear()

    @classmethod
    async def produce(cls, topic: str, key: str, value: dict[str, Any]) -> None:
        cls._topics[topic].append({"key": key, "value": value})

    @classmethod
    async def consume(cls, topic: str) -> list[dict[str, Any]]:
        return list(cls._topics.get(topic, []))

    @classmethod
    async def consume_one(cls, topic: str) -> dict[str, Any] | None:
        messages = cls._topics.get(topic, [])
        if messages:
            return messages.pop(0)
        return None


class KafkaProducer:
    """
    Продюсер — пишет события в Kafka.
    В тестах подменяется на InMemoryKafka.
    """

    def __init__(self, bootstrap_servers: str, use_mock: bool = False) -> None:
        self.bootstrap_servers = bootstrap_servers
        self._mock = use_mock
        self._producer: Any = None

    async def start(self) -> None:
        if self._mock:
            return
        try:
            from aiokafka import AIOKafkaProducer

            self._producer = AIOKafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode(),
                key_serializer=lambda k: k.encode() if k else None,
            )
            await self._producer.start()
        except Exception:
            self._mock = True  # fallback to mock if Kafka unavailable

    async def stop(self) -> None:
        if self._producer:
            await self._producer.stop()

    async def send(self, topic: str, key: str, value: dict[str, Any]) -> None:
        if self._mock:
            await InMemoryKafka.produce(topic, key, value)
            return
        await self._producer.send(topic, key=key, value=value)

    async def send_user_created(self, user_id: int, email: str) -> None:
        await self.send(
            topic="user.events",
            key=str(user_id),
            value={"event": "user_created", "user_id": user_id, "email": email},
        )

    async def send_user_deleted(self, user_id: int) -> None:
        await self.send(
            topic="user.events",
            key=str(user_id),
            value={"event": "user_deleted", "user_id": user_id},
        )
