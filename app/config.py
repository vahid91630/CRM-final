import os
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()

# توکن ربات تلگرام
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN تعریف نشده! مطمئن شو فایل .env در روت پروژه هست.")
