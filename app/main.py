from fastapi import FastAPI
from app.config import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bot is running", "webhook": settings.webhook_url}
