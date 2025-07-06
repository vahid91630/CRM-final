from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_async_session
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate, CustomerOut
from app.crud.customer_crud import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
)

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=CustomerOut)
async def create(customer: CustomerCreate, db: AsyncSession = Depends(get_async_session)):
    return await create_customer(db, customer)

@router.get("/{customer_id}", response_model=CustomerOut)
async def read(customer_id: int, db: AsyncSession = Depends(get_async_session)):
    customer = await get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return customer

@router.get("/", response_model=list[CustomerOut])
async def read_all(db: AsyncSession = Depends(get_async_session)):
    return await get_all_customers(db)

@router.put("/{customer_id}", response_model=CustomerOut)
async def update(customer_id: int, data: CustomerUpdate, db: AsyncSession = Depends(get_async_session)):
    updated = await update_customer(db, customer_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return updated

@router.delete("/{customer_id}")
async def delete(customer_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await delete_customer(db, customer_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return {"ok": True}
