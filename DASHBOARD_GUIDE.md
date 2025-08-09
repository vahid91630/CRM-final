# راهنمای استفاده از سیستم داشبورد و گزارشات

## مشکل حل شده ✅

مشکل نمایش دادن گزارشات در سیستم داشبورد و مانیتورینگ برطرف شد. سیستم اکنون شامل:

### قابلیت‌های جدید اضافه شده:

1. **داشبورد جامع** (`/dashboard/view`)
   - نمایش آمار کلی مشتریان
   - آمار مشتریان امروز، این هفته، این ماه
   - وضعیت سلامت سیستم
   - رابط کاربری فارسی با طراحی مدرن

2. **API های گزارشات** (`/dashboard/`)
   - `/dashboard/` - آمار کلی سیستم
   - `/dashboard/reports/customers` - گزارش جامع مشتریان
   - `/dashboard/monitoring/health` - مانیتورینگ سلامت سیستم
   - `/dashboard/reports/analytics` - گزارش تحلیلی پیشرفته

3. **مانیتورینگ سیستم**
   - بررسی وضعیت پایگاه داده
   - اندازه‌گیری زمان پاسخ
   - نمایش آمار عملکرد

## نحوه استفاده:

### نصب و راه‌اندازی:

```bash
# نصب وابستگی‌ها
pip install -r requirements.txt

# ایجاد داده‌های نمونه (اختیاری)
python create_sample_data.py

# اجرای سرور
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### دسترسی به داشبورد:

1. **رابط کاربری داشبورد**: http://localhost:8000/dashboard/view
2. **API داشبورد**: http://localhost:8000/dashboard/
3. **مستندات API**: http://localhost:8000/docs

### API Endpoints:

#### 1. آمار کلی داشبورد
```http
GET /dashboard/
```
پاسخ:
```json
{
  "status": "success",
  "data": {
    "total_customers": 15,
    "today_customers": 5,
    "week_customers": 10,
    "month_customers": 15,
    "last_updated": "2024-01-XX"
  }
}
```

#### 2. گزارش جامع مشتریان
```http
GET /dashboard/reports/customers
```
شامل:
- روند ثبت نام روزانه
- آمار ایمیل مشتریان
- لیست مشتریان اخیر

#### 3. مانیتورینگ سلامت سیستم
```http
GET /dashboard/monitoring/health
```
شامل:
- وضعیت سیستم
- زمان پاسخ پایگاه داده
- آمار عملکرد

#### 4. گزارش تحلیلی
```http
GET /dashboard/reports/analytics
```
شامل:
- روند رشد هفتگی
- ساعات پیک ثبت نام

## فایل‌های اضافه شده:

- `app/routers/dashboard_router.py` - روتر داشبورد و گزارشات
- `app/templates/dashboard.html` - رابط کاربری داشبورد
- `create_sample_data.py` - اسکریپت ایجاد داده نمونه
- `test_dashboard.py` - اسکریپت تست عملکرد

## ویژگی‌های داشبورد:

- ✅ نمایش آمار در زمان واقعی
- ✅ بروزرسانی خودکار هر 30 ثانیه
- ✅ طراحی ریسپانسیو
- ✅ پشتیبانی کامل از زبان فارسی
- ✅ نمایش وضعیت سلامت سیستم
- ✅ گزارشات تحلیلی پیشرفته

## تغییرات ایجاد شده:

1. **app/main.py**: اضافه شدن روتر داشبورد و تنظیمات CORS
2. **app/routers/customer_router.py**: بهبود کیفیت کد و اضافه شدن endpoint جدید
3. **app/routers/dashboard_router.py**: روتر جدید برای گزارشات و داشبورد
4. **app/templates/dashboard.html**: رابط کاربری داشبورد

مشکل گزارشات اکنون به طور کامل حل شده و سیستم آماده استفاده است! 🎉