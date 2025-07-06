from app.db.base import Base
from app.database import engine
import asyncio

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(
if __name__ == "__main__":
    asyncio.run(init_db())
