import os
import requests
from fastapi import APIRouter, Request
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# توکن ربات
BOT_TOKEN = "7847661218:AAEIHUcwg2gb7jF8zdK75w2Xk_exIewWAPU"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# پیام خوش‌آمد
WELCOME_MESSAGE = "سلام دوست عزیز! 😊 خوش اومدی. لطفاً اسم کامل خودت رو برام بنویس."

@router.post("/")
async def receive_message(req: Request):
    body = await req.json()
    
    if "message" in body:
        chat_id = body["message"]["chat"]["id"]
        text = body["message"].get("text", "")
        
        # پاسخ ساده به هر پیام
        send_message(chat_id, WELCOME_MESSAGE)

    return {"ok": True}


def send_message(chat_id: int, text: str):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)
