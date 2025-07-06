FROM python:3.11-slim

WORKDIR /app

# نصب وابستگی‌های سیستمی موردنیاز برای build پکیج‌ها
RUN apt-get update && \
    apt-get install -y gcc libpq-dev build-essential libffi-dev libssl-dev curl && \
    rm -rf /var/lib/apt/lists/*

# کپی فایل requirements و نصب پکیج‌ها
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# کپی کل پروژه
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
