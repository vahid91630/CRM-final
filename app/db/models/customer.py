from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, index=True)
    email = Column(String, nullable=True)
