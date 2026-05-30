import asyncio, os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def check():
    engine = create_async_engine(os.environ['DATABASE_URL'])
    async with engine.connect() as conn:
        result = await conn.execute(text('SELECT 1'))
        print('DB OK:', result.scalar())
    await engine.dispose()

asyncio.run(check())
