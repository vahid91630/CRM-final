from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate

async def get_customer(db: AsyncSession, customer_id: int) -> Customer | None:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    return result.scalar_one_or_none()

async def get_customers(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Customer]:
    result = await db.execute(select(Customer).offset(skip).limit(limit))
    return result.scalars().all()

async def create_customer(db: AsyncSession, customer: CustomerCreate) -> Customer:
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer

async def update_customer(db: AsyncSession, customer_id: int, updates: CustomerUpdate) -> Customer | None:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    db_customer = result.scalar_one_or_none()
    if db_customer:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        await db.commit()
        await db.refresh(db_customer)
    return db_customer

async def delete_customer(db: AsyncSession, customer_id: int) -> bool:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    db_customer = result.scalar_one_or_none()
    if db_customer:
        await db.delete(db_customer)
        await db.commit()
        return True
    return False
