from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import customer as models
from app.schemas import customer as schemas
from fastapi import Depends

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.post("/", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
