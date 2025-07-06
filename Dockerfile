FROM python:3.11-slim

# تنظیم encoding
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# نصب پیش‌نیازها برای کامپایل پکیج‌ها
RUN apt-get update && apt-get install -y build-essential gcc curl

# ساخت پوشه برای app
WORKDIR /app

# کپی کردن فایل‌ها
COPY . .

# نصب وابستگی‌ها
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# اجرای اپلیکیشن
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
