import uvicorn
from fastapi import FastAPI

from app.routers.customer import router as customer_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="CRM API")

# Register routes
app.include_router(customer_router)

# Auto create tables on startup
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
