from fastapi import FastAPI, Request
from app.bot.telegram import bot
from app.config import settings
import asyncio

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(req: Request):
    update = await req.json()
    await bot.process_new_updates([update])
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "CRM bot is live"}
