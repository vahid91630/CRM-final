import os
import requests
from fastapi import FastAPI, Request
from dotenv import load_dotenv

# بارگذاری فایل .env برای خواندن توکن و آدرس وب‌هوک
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# ساخت اپلیکیشن FastAPI
app = FastAPI()

# مسیر تستی (برای چک کردن سالم بودن سرور)
@app.get("/")
def read_root():
    return {"message": "CRM Bot is live and listening..."}

# مسیر اصلی دریافت پیام از تلگرام
@app.post(f"/{BOT_TOKEN}")
async def telegram_webhook(request: Request):
    data = await request.json()

    # گرفتن اطلاعات پیام
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    user_text = message.get("text", "")

    # واکنش ساده به پیام
    reply_text = f"📥 پیام شما دریافت شد:\n\n{user_text}"

    # ارسال پاسخ به تلگرام
    if chat_id:
        send_message(chat_id, reply_text)

    return {"ok": True}

# تابع کمکی برای ارسال پیام به تلگرام
def send_message(chat_id: int, text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()
