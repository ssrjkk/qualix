import asyncio
import os
import sys

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from app.models.db import Base


async def check():
    url = os.environ["DATABASE_URL"]
    print(f"Connecting to: {url}")

    engine = create_async_engine(url)
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("DB ping OK:", result.scalar())
    await engine.dispose()

    engine2 = create_async_engine(url)
    async with engine2.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Table creation OK")
    await engine2.dispose()

    print("All DB checks passed")


if __name__ == "__main__":
    try:
        asyncio.run(check())
    except Exception as exc:
        print(f"DB CHECK FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
