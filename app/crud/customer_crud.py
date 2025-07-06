from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.customer import Customer
from app.schemas.customer_schema import CustomerCreate

async def create_customer(db: AsyncSession, customer: CustomerCreate) -> Customer:
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer

async def get_customer_by_id(db: AsyncSession, customer_id: int) -> Customer | None:
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    return result.scalar_one_or_none()

async def get_all_customers(db: AsyncSession) -> list[Customer]:
    result = await db.execute(select(Customer))
    return result.scalars().all()
