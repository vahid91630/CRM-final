from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.customer import CustomerCreate, CustomerOut
from app.db.database import get_db
from app.models import models
from app.crud import customer as customer_crud

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerOut)
async def create_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db)):
    existing_customer = await customer_crud.get_customer_by_telegram_id(db, customer.telegram_id)
    if existing_customer:
        raise HTTPException(status_code=400, detail="Customer already exists.")
    return await customer_crud.create_customer(db=db, customer=customer)

@router.get("/{telegram_id}", response_model=CustomerOut)
async def get_customer(telegram_id: int, db: AsyncSession = Depends(get_db)):
    customer = await customer_crud.get_customer_by_telegram_id(db, telegram_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found.")
    return customer
