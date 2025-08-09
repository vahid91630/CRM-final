from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import get_db
from app.db.models.customer import Customer
from typing import List, Dict, Any

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/")
async def get_customers(db: AsyncSession = Depends(get_db)):
    """دریافت لیست تمام مشتریان - Get all customers"""
    try:
        result = await db.execute(text("SELECT * FROM customers"))
        customers = result.fetchall()
        
        # Convert to list of dictionaries
        customers_list = []
        for customer in customers:
            customers_list.append({
                "id": customer.id,
                "full_name": customer.full_name,
                "phone_number": customer.phone_number,
                "email": customer.email,
                "created_at": customer.created_at.isoformat() if customer.created_at else None
            })
        
        return {
            "status": "success",
            "data": customers_list,
            "count": len(customers_list),
            "message": "لیست مشتریان با موفقیت دریافت شد"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطا در دریافت لیست مشتریان: {str(e)}")

@router.get("/count")
async def get_customers_count(db: AsyncSession = Depends(get_db)):
    """دریافت تعداد کل مشتریان - Get total customers count"""
    try:
        result = await db.execute(text("SELECT COUNT(*) as count FROM customers"))
        count = result.scalar()
        
        return {
            "status": "success", 
            "data": {"total_customers": count or 0},
            "message": "تعداد مشتریان با موفقیت محاسبه شد"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"خطا در محاسبه تعداد مشتریان: {str(e)}")
