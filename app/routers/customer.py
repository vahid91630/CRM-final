from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerRead
from typing import List

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=CustomerRead)
async def create_customer(
    customer: CustomerCreate,
    db: AsyncSession = Depends(get_db)
):
    new_customer = Customer(
        full_name=customer.full_name,
        phone_number=customer.phone_number,
        email=customer.email
    )
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    return new_customer

@router.get("/", response_model=List[CustomerRead])
async def get_customers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Customer))
    customers = result.scalars().all()
    return customers

@router.get("/{customer_id}", response_model=CustomerRead)
async def get_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalar_one_or_none()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.delete("/{customer_id}")
async def delete_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalar_one_or_none()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    await db.delete(customer)
    await db.commit()
    return {"detail": "Customer deleted"}
