from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/customers", tags=["Customers"])

class Customer(BaseModel):
    name: str
    phone: str
    email: str = None

fake_db = []

@router.post("/")
async def create_customer(customer: Customer):
    fake_db.append(customer)
    return {"msg": "Customer added", "customer": customer}

@router.get("/")
async def list_customers():
    return fake_db
