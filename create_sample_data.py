#!/usr/bin/env python3
"""
اسکریپت تولید داده‌های نمونه برای تست سیستم
Sample data generation script for testing the system
"""

import asyncio
import sqlite3
from datetime import datetime, timedelta
import random

def create_sample_data():
    """Create sample customer data for testing dashboard"""
    
    # Connect to SQLite database
    conn = sqlite3.connect('./app.db')
    cursor = conn.cursor()
    
    # Create customers table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            phone_number TEXT UNIQUE NOT NULL,
            email TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Sample customer data
    sample_customers = [
        ('احمد محمدی', '09121234567', 'ahmad.mohammadi@email.com'),
        ('فاطمه احمدی', '09121234568', 'fateme.ahmadi@email.com'),
        ('علی رضایی', '09121234569', None),
        ('مریم حسینی', '09121234570', 'maryam.hosseini@email.com'),
        ('محمد علیزاده', '09121234571', None),
        ('زهرا کریمی', '09121234572', 'zahra.karimi@email.com'),
        ('حسن باقری', '09121234573', 'hasan.bagheri@email.com'),
        ('سارا موسوی', '09121234574', None),
        ('رضا نوری', '09121234575', 'reza.nouri@email.com'),
        ('لیلا صادقی', '09121234576', 'leila.sadeghi@email.com'),
        ('امیر تهرانی', '09121234577', None),
        ('نرگس اصفهانی', '09121234578', 'narges.esfahani@email.com'),
        ('بهزاد شیرازی', '09121234579', 'behzad.shirazi@email.com'),
        ('شیما تبریزی', '09121234580', None),
        ('مجید کردی', '09121234581', 'majid.kordi@email.com')
    ]
    
    # Insert sample customers with different dates
    base_date = datetime.now()
    
    for i, (name, phone, email) in enumerate(sample_customers):
        # Distribute customers across different time periods
        if i < 5:
            # Today
            created_date = base_date
        elif i < 10:
            # This week
            days_ago = random.randint(1, 6)
            created_date = base_date - timedelta(days=days_ago)
        else:
            # Older dates
            days_ago = random.randint(7, 30)
            created_date = base_date - timedelta(days=days_ago)
        
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO customers (full_name, phone_number, email, created_at)
                VALUES (?, ?, ?, ?)
            ''', (name, phone, email, created_date.isoformat()))
        except sqlite3.IntegrityError:
            # Skip if phone number already exists
            pass
    
    conn.commit()
    
    # Print summary
    cursor.execute('SELECT COUNT(*) FROM customers')
    total_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM customers WHERE DATE(created_at) = DATE("now")')
    today_count = cursor.fetchone()[0]
    
    print(f"✅ داده‌های نمونه ایجاد شد:")
    print(f"   کل مشتریان: {total_count}")
    print(f"   مشتریان امروز: {today_count}")
    
    conn.close()

if __name__ == "__main__":
    create_sample_data()