FROM python:3.12-slim

LABEL maintainer="ssrjkk" org.opencontainers.image.authors="ssrjkk"

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/* && pip install uv --no-cache-dir

COPY pyproject.toml README.md .
COPY app/ app/
COPY frontend/ frontend/

RUN uv pip install --system "."

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

EXPOSE 8080

CMD ["/app/docker-entrypoint.sh"]
