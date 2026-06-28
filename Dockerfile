FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/* && pip install uv --no-cache-dir

COPY pyproject.toml .
COPY app/ app/
COPY frontend/ frontend/

RUN uv pip install --system -e "."

EXPOSE 8080

CMD ["python", "-m", "app.entrypoint"]
