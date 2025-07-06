from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.session import get_session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerRead

router = APIRouter()

@router.post("/", response_model=CustomerRead)
async def create_customer(
    customer: CustomerCreate,
    session: AsyncSession = Depends(get_session)
):
    db_customer = Customer(**customer.dict())
    session.add(db_customer)
    await session.commit()
    await session.refresh(db_customer)
    return db_customer

@router.get("/", response_model=list[CustomerRead])
async def get_customers(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Customer))
    return result.scalars().all()
