import os
import logging
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from dotenv import load_dotenv

# .env مقادیر محیطی رو بارگذاری کن
load_dotenv()

# لاگ‌گذاری حرفه‌ای
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    logger.info("🌐 Bot is starting...")
    webhook_url = os.getenv("WEBHOOK_URL")
    if webhook_url:
        await bot.set_webhook(webhook_url)
        logger.info(f"Webhook set to {webhook_url}")
    else:
        logger.warning("WEBHOOK_URL is not set in .env")

@app.post("/bot")
async def telegram_webhook(request: Request):
    body = await request.json()
    logger.debug(f"📨 Incoming update: {body}")
    update = Update.to_object(body)
    await dp.process_update(update)
    return {"ok": True}
