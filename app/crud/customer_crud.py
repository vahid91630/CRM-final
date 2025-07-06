from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.customer import Customer
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate

async def create_customer(db: AsyncSession, customer: CustomerCreate) -> Customer:
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    return new_customer

async def get_customer(db: AsyncSession, customer_id: int) -> Customer | None:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    return result.scalars().first()

async def get_all_customers(db: AsyncSession) -> list[Customer]:
    result = await db.execute(select(Customer))
    return result.scalars().all()

async def update_customer(db: AsyncSession, customer_id: int, updates: CustomerUpdate) -> Customer | None:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalars().first()
    if customer:
        for field, value in updates.dict(exclude_unset=True).items():
            setattr(customer, field, value)
        await db.commit()
        await db.refresh(customer)
    return customer

async def delete_customer(db: AsyncSession, customer_id: int) -> bool:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalars().first()
    if customer:
        await db.delete(customer)
        await db.commit()
        return True
    return False
