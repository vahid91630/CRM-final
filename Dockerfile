FROM python:3.11-slim

WORKDIR /app

# نصب پیش‌نیازهای سیستمی برای کامپایل
RUN apt-get update && \
    apt-get install -y gcc libpq-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# نصب پکیج‌های پایتونی
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# کپی کامل پروژه
COPY . .

# اجرای اپلیکیشن
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
