from fastapi import FastAPI, Request
from bot.telegram import dp, bot
import asyncio
import os
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiogram.webhook.dispatcher import AiogramWebhook
from aiogram.webhook.base import BaseWebhookRequestHandler
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    webhook_url = os.getenv("WEBHOOK_URL")
    await bot.set_webhook(webhook_url)

SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
