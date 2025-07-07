from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.models.customer import Customer

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/")
async def get_customers(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM customers")
    return result.fetchall()
