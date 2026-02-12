"""
OpenAPI схема — экспортируется для schemathesis.
Запуск: python -m app.api.openapi > openapi.json
"""
from __future__ import annotations

import json, sys
from app.main import create_app

if __name__ == "__main__":
    app = create_app()
    print(json.dumps(app.openapi(), indent=2))
