from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate

async def create_customer(db: AsyncSession, customer: CustomerCreate):
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    return new_customer

async def get_customer(db: AsyncSession, customer_id: int):
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    return result.scalars().first()

async def get_customers(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Customer).offset(skip).limit(limit))
    return result.scalars().all()

async def update_customer(db: AsyncSession, customer_id: int, customer: CustomerUpdate):
    db_customer = await get_customer(db, customer_id)
    if not db_customer:
        return None
    for key, value in customer.dict(exclude_unset=True).items():
        setattr(db_customer, key, value)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer

async def delete_customer(db: AsyncSession, customer_id: int):
    db_customer = await get_customer(db, customer_id)
    if not db_customer:
        return None
    await db.delete(db_customer)
    await db.commit()
    return db_customer
