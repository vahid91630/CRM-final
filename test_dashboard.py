#!/usr/bin/env python3
"""
تست اندپوینت‌های داشبورد
Dashboard endpoints testing script
"""

import asyncio
import json
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import async_session, engine
from app.db.base import Base
from app.routers.dashboard_router import get_dashboard_overview, get_customer_reports, get_system_health

async def test_dashboard_endpoints():
    """Test all dashboard endpoints"""
    
    print("🧪 شروع تست اندپوینت‌های داشبورد...")
    
    # Create tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Create a database session
    async with async_session() as db:
        try:
            # Test dashboard overview
            print("\n📊 تست آمار کلی داشبورد...")
            overview_result = await get_dashboard_overview(db)
            print(f"✅ نتیجه آمار کلی: {json.dumps(overview_result, ensure_ascii=False, indent=2)}")
            
            # Test customer reports
            print("\n📈 تست گزارش مشتریان...")
            reports_result = await get_customer_reports(db)
            print(f"✅ نتیجه گزارش مشتریان: تعداد آمار روزانه: {len(reports_result['data']['daily_registrations'])}")
            print(f"   مشتریان با ایمیل: {reports_result['data']['email_statistics']['with_email']}")
            print(f"   مشتریان اخیر: {len(reports_result['data']['recent_customers'])}")
            
            # Test system health
            print("\n🏥 تست سلامت سیستم...")
            health_result = await get_system_health(db)
            print(f"✅ نتیجه سلامت سیستم: {health_result['data']['system_status']}")
            print(f"   وضعیت پایگاه داده: {health_result['data']['database']['status']}")
            
            print("\n🎉 همه تست‌ها با موفقیت انجام شد!")
            
        except Exception as e:
            print(f"❌ خطا در تست: {str(e)}")
            raise

if __name__ == "__main__":
    asyncio.run(test_dashboard_endpoints())