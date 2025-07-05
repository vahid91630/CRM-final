from fastapi import FastAPI
from app.db import models, database
from app.routers import customers
from app.bot.telegram import start_bot

app = FastAPI(title="CRM API", version="1.0")

# ایجاد جداول دیتابیس
models.Base.metadata.create_all(bind=database.engine)

# ثبت روت‌ها
app.include_router(customers.router)

# پیام خوش‌آمد در روت اصلی
@app.get("/")
def root():
    return {"message": "✅ CRM API فعال است. مستندات در /docs قابل مشاهده است."}

# راه‌اندازی بات تلگرام هنگام استارت پروژه
@app.on_event("startup")
async def on_startup():
    start_bot()
