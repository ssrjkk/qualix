#!/bin/sh
set -e

echo "[entrypoint] Python version: $(python --version)"
echo "[entrypoint] Testing import..."
python -c "
import sys, traceback
try:
    from app.main import app
    print('[entrypoint] Import OK')
except Exception:
    traceback.print_exc(file=sys.stdout)
    sys.stdout.flush()
    sys.exit(1)
"

echo "[entrypoint] Starting uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8080 --log-level debug
