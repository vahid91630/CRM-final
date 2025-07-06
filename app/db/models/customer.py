from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base

class Customer(Base):
    __tablename__ = "customers"

    id: int = Column(Integer, primary_key=True, index=True)
    full_name: str = Column(String(100), nullable=False)
    phone_number: str = Column(String(20), unique=True, nullable=False)
    email: str = Column(String(100), nullable=True)
    created_at: DateTime = Column(DateTime(timezone=True), server_default=func.now())
