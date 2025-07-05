from fastapi import APIRouter, Request
import httpx
from app.config import BOT_TOKEN

telegram_router = APIRouter()

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@telegram_router.post("/")
async def receive_update(update: dict):
    message = update.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if not chat_id or not text:
        return {"ok": False, "message": "داده نامعتبر"}

    response_text = f"✅ پیام شما دریافت شد:\n{text}"

    async with httpx.AsyncClient() as client:
        await client.post(f"{TELEGRAM_API_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": response_text
        })

    return {"ok": True}
