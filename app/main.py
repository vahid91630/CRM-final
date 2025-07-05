from fastapi import FastAPI
from app.bot.telegram import dp, bot

app = FastAPI()

@app.on_event("startup")
async def startup():
    await bot.set_webhook(os.getenv("WEBHOOK_URL"))
