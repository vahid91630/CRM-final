from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, func
from app.db.session import get_db
from app.db.models.customer import Customer
from datetime import datetime, timedelta
from typing import Dict, Any
import logging
import os

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

logger = logging.getLogger(__name__)

@router.get("/view", response_class=HTMLResponse)
async def dashboard_view():
    """
    نمایش صفحه داشبورد
    Display dashboard HTML page
    """
    try:
        template_path = os.path.join(os.path.dirname(__file__), "..", "templates", "dashboard.html")
        with open(template_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="صفحه داشبورد یافت نشد")
    except Exception as e:
        logger.error(f"Error serving dashboard view: {str(e)}")
        raise HTTPException(status_code=500, detail="خطا در نمایش داشبورد")

@router.get("/")
async def get_dashboard_overview(db: AsyncSession = Depends(get_db)):
    """
    داشبورد اصلی - نمایش خلاصه آمار سیستم
    Main dashboard - Display system overview statistics
    """
    try:
        # Get total customers
        total_customers_result = await db.execute(
            text("SELECT COUNT(*) as count FROM customers")
        )
        total_customers = total_customers_result.scalar()

        # Get customers registered today
        today = datetime.now().date()
        today_customers_result = await db.execute(
            text("SELECT COUNT(*) as count FROM customers WHERE DATE(created_at) = :today"),
            {"today": today}
        )
        today_customers = today_customers_result.scalar()

        # Get customers registered this week
        week_ago = datetime.now() - timedelta(days=7)
        week_customers_result = await db.execute(
            text("SELECT COUNT(*) as count FROM customers WHERE created_at >= :week_ago"),
            {"week_ago": week_ago}
        )
        week_customers = week_customers_result.scalar()

        # Get customers registered this month
        month_ago = datetime.now() - timedelta(days=30)
        month_customers_result = await db.execute(
            text("SELECT COUNT(*) as count FROM customers WHERE created_at >= :month_ago"),
            {"month_ago": month_ago}
        )
        month_customers = month_customers_result.scalar()

        return {
            "status": "success",
            "data": {
                "total_customers": total_customers or 0,
                "today_customers": today_customers or 0,
                "week_customers": week_customers or 0,
                "month_customers": month_customers or 0,
                "last_updated": datetime.now().isoformat()
            },
            "message": "آمار داشبورد با موفقیت بارگذاری شد"
        }

    except Exception as e:
        logger.error(f"Error fetching dashboard overview: {str(e)}")
        raise HTTPException(status_code=500, detail="خطا در بارگذاری آمار داشبورد")

@router.get("/reports/customers")
async def get_customer_reports(db: AsyncSession = Depends(get_db)):
    """
    گزارش جامع مشتریان
    Comprehensive customer reports
    """
    try:
        # Get daily registration trend for last 30 days
        thirty_days_ago = datetime.now() - timedelta(days=30)
        daily_trend_result = await db.execute(
            text("""
                SELECT 
                    DATE(created_at) as date,
                    COUNT(*) as count
                FROM customers 
                WHERE created_at >= :thirty_days_ago
                GROUP BY DATE(created_at)
                ORDER BY date DESC
            """),
            {"thirty_days_ago": thirty_days_ago}
        )
        daily_trend = [
            {"date": str(row.date), "count": row.count} 
            for row in daily_trend_result.fetchall()
        ]

        # Get customers with emails vs without emails
        with_email_result = await db.execute(
            text("SELECT COUNT(*) as count FROM customers WHERE email IS NOT NULL AND email != ''")
        )
        with_email = with_email_result.scalar()

        without_email_result = await db.execute(
            text("SELECT COUNT(*) as count FROM customers WHERE email IS NULL OR email = ''")
        )
        without_email = without_email_result.scalar()

        # Get recent customers (last 10)
        recent_customers_result = await db.execute(
            text("""
                SELECT full_name, phone_number, email, created_at
                FROM customers
                ORDER BY created_at DESC
                LIMIT 10
            """)
        )
        recent_customers = [
            {
                "full_name": row.full_name,
                "phone_number": row.phone_number,
                "email": row.email,
                "created_at": row.created_at.isoformat() if row.created_at else None
            }
            for row in recent_customers_result.fetchall()
        ]

        return {
            "status": "success",
            "data": {
                "daily_registrations": daily_trend,
                "email_statistics": {
                    "with_email": with_email or 0,
                    "without_email": without_email or 0
                },
                "recent_customers": recent_customers,
                "generated_at": datetime.now().isoformat()
            },
            "message": "گزارش مشتریان با موفقیت تولید شد"
        }

    except Exception as e:
        logger.error(f"Error generating customer reports: {str(e)}")
        raise HTTPException(status_code=500, detail="خطا در تولید گزارش مشتریان")

@router.get("/monitoring/health")
async def get_system_health(db: AsyncSession = Depends(get_db)):
    """
    مانیتورینگ سلامت سیستم
    System health monitoring
    """
    try:
        # Test database connection
        db_status = "healthy"
        db_response_time = None
        
        start_time = datetime.now()
        try:
            await db.execute(text("SELECT 1"))
            end_time = datetime.now()
            db_response_time = (end_time - start_time).total_seconds() * 1000  # milliseconds
        except Exception as e:
            db_status = "unhealthy"
            logger.error(f"Database health check failed: {str(e)}")

        # Get system statistics
        try:
            stats_result = await db.execute(
                text("SELECT COUNT(*) as total_records FROM customers")
            )
            total_records = stats_result.scalar()
        except:
            total_records = 0

        return {
            "status": "success",
            "data": {
                "system_status": "operational" if db_status == "healthy" else "degraded",
                "database": {
                    "status": db_status,
                    "response_time_ms": db_response_time,
                },
                "statistics": {
                    "total_customers": total_records or 0
                },
                "timestamp": datetime.now().isoformat()
            },
            "message": "وضعیت سلامت سیستم بررسی شد"
        }

    except Exception as e:
        logger.error(f"Error checking system health: {str(e)}")
        return {
            "status": "error",
            "data": {
                "system_status": "error",
                "database": {"status": "unknown"},
                "timestamp": datetime.now().isoformat()
            },
            "message": "خطا در بررسی وضعیت سیستم"
        }

@router.get("/reports/analytics")
async def get_analytics_report(db: AsyncSession = Depends(get_db)):
    """
    گزارش تحلیلی پیشرفته
    Advanced analytics report
    """
    try:
        # Customer growth trend (weekly)
        growth_result = await db.execute(
            text("""
                SELECT 
                    strftime('%Y-%W', created_at) as week,
                    COUNT(*) as count
                FROM customers 
                WHERE created_at >= datetime('now', '-12 weeks')
                GROUP BY week
                ORDER BY week
            """)
        )
        growth_trend = [
            {"week": row.week, "count": row.count}
            for row in growth_result.fetchall()
        ]

        # Peak registration hours
        peak_hours_result = await db.execute(
            text("""
                SELECT 
                    strftime('%H', created_at) as hour,
                    COUNT(*) as count
                FROM customers
                GROUP BY hour
                ORDER BY count DESC
                LIMIT 5
            """)
        )
        peak_hours = [
            {"hour": int(row.hour), "count": row.count}
            for row in peak_hours_result.fetchall()
        ]

        return {
            "status": "success",
            "data": {
                "growth_trend": growth_trend,
                "peak_registration_hours": peak_hours,
                "generated_at": datetime.now().isoformat()
            },
            "message": "گزارش تحلیلی با موفقیت تولید شد"
        }

    except Exception as e:
        logger.error(f"Error generating analytics report: {str(e)}")
        raise HTTPException(status_code=500, detail="خطا در تولید گزارش تحلیلی")