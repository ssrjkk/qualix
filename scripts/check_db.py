import asyncio
import os

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine


async def check():
    engine = create_async_engine(os.environ["DATABASE_URL"])
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("DB OK:", result.scalar())
    await engine.dispose()


asyncio.run(check())
