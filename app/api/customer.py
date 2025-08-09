from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.customer import CustomerCreate, CustomerOut
from app.db.session import get_db
from app.crud import customer_crud

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerOut)
async def create_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db)):
    existing_customer = await customer_crud.get_customer_by_telegram_id(db, customer.id if hasattr(customer, 'id') else 0)
    if existing_customer:
        raise HTTPException(status_code=400, detail="Customer already exists.")
    return await customer_crud.create_customer(db=db, customer=customer)

@router.get("/{customer_id}", response_model=CustomerOut)
async def get_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    customer = await customer_crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found.")
    return customer
