from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.customer import Customer, CustomerCreate, CustomerUpdate
from app.crud import customer as crud_customer

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/", response_model=list[Customer])
async def read_customers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_customer.get_customers(db, skip=skip, limit=limit)

@router.get("/{customer_id}", response_model=Customer)
async def read_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    db_customer = await crud_customer.get_customer(db, customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.post("/", response_model=Customer)
async def create_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db)):
    return await crud_customer.create_customer(db, customer)

@router.put("/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, updates: CustomerUpdate, db: AsyncSession = Depends(get_db)):
    updated_customer = await crud_customer.update_customer(db, customer_id, updates)
    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/{customer_id}")
async def delete_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud_customer.delete_customer(db, customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted"}
