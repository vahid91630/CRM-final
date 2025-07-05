import os
from fastapi import FastAPI
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()

# ایمپورت تنظیمات و ماژول‌های داخلی
from app.db import database, models
from app.bot.telegram_bot import telegram_router

# تعریف اپلیکیشن FastAPI
app = FastAPI()

# اتصال و قطع اتصال دیتابیس در شروع/پایان
@app.on_event("startup")
async def startup():
    await database.database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()

# مسیر ریشه
@app.get("/")
def root():
    return {
        "message": "🎯 CRM API آماده است. برای مستندات API برو به: /docs"
    }

# اضافه کردن مسیر ربات تلگرام
app.include_router(telegram_router, prefix="/bot")
