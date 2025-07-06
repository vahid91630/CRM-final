from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    telegram_id: int

class CustomerCreate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int

    class Config:
        orm_mode = True
