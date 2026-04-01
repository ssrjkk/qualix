# ADR 003: bcrypt вместо SHA-256 для хеширования паролей

**Статус:** Accepted  
**Дата:** 2026-02-01  
**Автор:** Ситников Сергей

## Контекст

Первоначальная реализация использовала `hashlib.sha256` для хеширования паролей.

## Проблема

SHA-256 небезопасен для паролей:
- **Нет соли** → уязвим к rainbow table атакам
- **Слишком быстрый** → GPU может перебрать миллиарды хешей/сек
- **Детерминирован** → одинаковый пароль = одинаковый хеш

## Решение

`bcrypt` через пакет `bcrypt`:
```python
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt).decode()
```

## Обоснование

- **Автоматическая соль**: каждый хеш уникален даже для одинакового пароля
- **Cost factor (rounds=12)**: ~250ms на современном CPU — достаточно медленно для brute-force
- **Constant-time verify**: `bcrypt.checkpw` защищает от timing attacks
- **OWASP рекомендация**: bcrypt с rounds≥10 для новых проектов

## Последствия

- Логин стал медленнее (~250ms вместо <1ms)
- Benchmark тесты теперь проверяют что `rounds=12` используется
- Mock тесты обновлены: `hash_password("Pass1!")` вместо `hashlib.sha256(...)`
