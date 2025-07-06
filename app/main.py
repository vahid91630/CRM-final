import os
from fastapi import FastAPI
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app.routers import customer

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    environment="production"
)

app = FastAPI()
app = SentryAsgiMiddleware(app)

app.include_router(customer.router)

@app.get("/")
async def root():
    return {"message": "CRM running"}

@app.get("/crash")
async def crash():
    raise Exception("Test Error")
