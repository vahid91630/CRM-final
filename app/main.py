import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.customer_router import router as customer_router
from app.routers.dashboard_router import router as dashboard_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI(
    title="CRM API",
    description="سیستم مدیریت ارتباط با مشتری - Customer Relationship Management System",
    version="1.0.0"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(customer_router)
app.include_router(dashboard_router)

# Auto create tables on startup
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
