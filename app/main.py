from fastapi import FastAPI
from app.routers import customer

app = FastAPI()

app.include_router(customer.router)

@app.get("/")
async def root():
    return {"message": "CRM Bot is running"}
