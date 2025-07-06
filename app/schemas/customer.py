from pydantic import BaseModel

class CustomerBase(BaseModel):
    full_name: str
    phone_number: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CustomerRead(CustomerBase):
    id: int

    class Config:
        orm_mode = True
