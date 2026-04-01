# ADR 004: fakeredis вместо unittest.mock для Redis тестов

**Статус:** Accepted  
**Дата:** 2026-02-10  
**Автор:** Ситников Сергей

## Контекст

Тесты Redis-зависимого кода. Варианты:
1. `unittest.mock.AsyncMock` — мокируем redis клиент
2. `fakeredis` — in-memory Redis реализация
3. Реальный Redis через testcontainers

## Решение

`fakeredis.aioredis` — полная in-memory реализация Redis API.

## Обоснование

**Против mock:**
- Мок не проверяет реальное поведение Redis команд
- TTL, INCR, HSET — сложно мокировать правильно
- При изменении кода мок может давать false positive

**За fakeredis:**
- Реальный Redis API без Docker зависимости
- TTL, pub/sub, hash операции работают как настоящий Redis
- Тесты запускаются в любой среде

**Реальный Redis (testcontainers):**
- Используется в CI когда Docker доступен
- `@pytest.mark.skipif(not REAL_REDIS_UP)` — один тест для smoke check

## Последствия

- `fakeredis>=2.26` в test зависимостях
- Redis тесты работают локально без Docker
- 3 Redis теста пропускаются без реального Redis (ожидаемо)
