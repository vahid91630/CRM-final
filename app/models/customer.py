from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    telegram_id = Column(Integer, unique=True, index=True, nullable=False)
