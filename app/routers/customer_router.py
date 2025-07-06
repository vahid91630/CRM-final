from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import session
from app.models import customer
from app.schemas import customer_schema

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=customer_schema.CustomerOut)
async def create_customer(
    customer_data: customer_schema.CustomerCreate,
    db: AsyncSession = Depends(session.get_session)
):
    return await customer.create_customer(db, customer_data)

@router.get("/", response_model=list[customer_schema.CustomerOut])
async def get_all_customers(
    db: AsyncSession = Depends(session.get_session)
):
    return await customer.get_all_customers(db)

@router.get("/{customer_id}", response_model=customer_schema.CustomerOut)
async def get_customer_by_id(
    customer_id: int,
    db: AsyncSession = Depends(session.get_session)
):
    return await customer.get_customer_by_id(db, customer_id)

@router.delete("/{customer_id}")
async def delete_customer(
    customer_id: int,
    db: AsyncSession = Depends(session.get_session)
):
    return await customer.delete_customer(db, customer_id)
