# ADR 002: SQLite in-memory fallback для тестов без Docker

**Статус:** Accepted  
**Дата:** 2026-01-20  
**Автор:** Ситников Сергей

## Контекст

Integration и API тесты требуют реальную базу данных.
Варианты запуска:
1. Только через Docker (testcontainers)
2. SQLite fallback когда Docker недоступен

## Решение

Автодетект Docker через `socket.connect("/var/run/docker.sock")`.
- Docker доступен → testcontainers с Postgres 16
- Docker недоступен → SQLite через aiosqlite (файловый, не in-memory)

## Обоснование

**Проблема in-memory SQLite:** каждый `create_engine()` создаёт новую БД.
Session-scope `client` и `db_engine` фикстуры создавали разные engines —
таблицы создавались в одной БД, запросы шли в другую.

**Решение:** файловый SQLite + `_shared_engine` singleton в `dependencies.py`.
Файл удаляется перед каждым прогоном через `_clean_sqlite_db` autouse фикстуру.

## Последствия

- `testcontainers` — только в CI или при локальном Docker
- SQLite не поддерживает все фичи Postgres (например, некоторые типы)
- `begin_nested()` (savepoints) работает по-другому в SQLite → тест дубликата
  использует отдельную сессию с `commit()`

## Альтернативы рассмотрены

- `pytest-postgresql` + embedded postgres: сложная установка
- `asyncpg` mock: теряем реальное поведение SQL
