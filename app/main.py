from fastapi import FastAPI
from bot.telegram import dp, bot

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    print("Bot starting...")


@app.get("/")
async def root():
    return {"status": "OK"}
