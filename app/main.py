import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database models & config (adjusted for being inside 'app/')
from db import models, database

# Telegram Bot router (inside bot/)
from bot.telegram_bot import telegram_router

# Initialize FastAPI app
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()

# Root route
@app.get("/")
def root():
    return {"message": "✅ CRM API فعال است. برای تست API به مسیر /docs بروید."}

# Register Telegram router
app.include_router(telegram_router, prefix="/bot")
