import os
import requests
from fastapi import APIRouter, Request
from dotenv import load_dotenv

from bot.handlers import handle_text_message

load_dotenv()

router = APIRouter()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


@router.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()

    message = data.get("message")
    if not message:
        return {"status": "no message"}

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    response_text = handle_text_message(chat_id, text)
    send_message(chat_id, response_text)

    return {"status": "ok"}


def send_message(chat_id: int, text: str) -> None:
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Error sending message:", e)
