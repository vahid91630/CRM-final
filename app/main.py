from fastapi import FastAPI
from app.config import settings
from app.bot.telegram_bot import bot_router
from app.db.session import engine
from app.db.base import Base
import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(bot_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
