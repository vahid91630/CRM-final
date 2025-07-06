from fastapi import FastAPI
from app.routes.customer import router as customer_router
from app.db.database import engine, Base
import asyncio
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(customer_router, prefix="/customers")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
