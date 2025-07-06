FROM python:3.11-slim

WORKDIR /app

# نصب دیپندنسی‌های سیستمی برای build و پکیج‌هایی مثل aiohttp، uvicorn، yarl
RUN apt-get update && \
    apt-get install -y gcc libpq-dev build-essential libffi-dev \
                       libssl-dev curl && \
    rm -rf /var/lib/apt/lists/*

# کپی فایل پکیج‌ها
COPY requirements.txt .

# نصب پکیج‌ها
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# کپی فایل‌های پروژه
COPY . .

# اجرای اپلیکیشن
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
