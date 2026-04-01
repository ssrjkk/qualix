# ADR 005: JSON Schema контракты вместо Pact

**Статус:** Accepted  
**Дата:** 2026-02-15  
**Автор:** Ситников Сергей

## Контекст

Contract testing — проверка соответствия API ожиданиям consumer.
Варианты:
1. **Pact** — consumer-driven contract testing с Pact Broker
2. **JSON Schema validation** — кастомные контракты в коде

## Решение

JSON Schema контракты (`tests/contract/test_api_contracts.py`).

## Обоснование

**Против Pact в данном проекте:**
- Требует запущенный Pact Broker (отдельный сервис)
- `pact-python` v2 нестабилен, сложная установка
- Избыточен когда consumer и provider — одна команда

**За JSON Schema:**
- Нулевые внешние зависимости
- Контракты читаемы как документация
- Security контракт (`not_allowed_fields: [password]`) — явная защита
- Легко расширять: добавить новый контракт = добавить dict

## Контракты покрывают

- `user_response` — shape + security (нет password в ответе)
- `user_list_response` — pagination структура
- `token_response` — auth token format
- `error_response` — error shape consistency

## Миграция на Pact

Когда проект вырастет до нескольких команд:
```bash
pip install pact-python
# Заменить dict-валидацию на Pact Consumer DSL
```
