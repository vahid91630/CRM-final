from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_async_session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerRead

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerRead)
async def create_customer(
    customer: CustomerCreate,
    session: AsyncSession = Depends(get_async_session)
):
    db_customer = Customer(**customer.dict())
    session.add(db_customer)
    await session.commit()
    await session.refresh(db_customer)
    return db_customer

@router.get("/", response_model=list[CustomerRead])
async def get_all_customers(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Customer))
    customers = result.scalars().all()
    return customers

@router.get("/{customer_id}", response_model=CustomerRead)
async def get_customer(customer_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalars().first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
