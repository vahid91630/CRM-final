#!/bin/bash

echo "🚀 راه‌اندازی سیستم CRM Dashboard..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 ایجاد محیط مجازی..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 فعال‌سازی محیط مجازی..."
source venv/bin/activate

# Install requirements
echo "⬇️ نصب وابستگی‌ها..."
pip install -r requirements.txt

# Create sample data if database doesn't exist
if [ ! -f "app.db" ]; then
    echo "📊 ایجاد داده‌های نمونه..."
    python create_sample_data.py
fi

echo "✅ آماده‌سازی کامل شد!"
echo ""
echo "🌐 برای دسترسی به داشبورد:"
echo "   http://localhost:8000/dashboard/view"
echo ""
echo "📚 برای مستندات API:"
echo "   http://localhost:8000/docs"
echo ""
echo "🎯 شروع سرور..."

# Start the server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload