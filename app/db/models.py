from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20), unique=True)
