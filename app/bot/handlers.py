from typing import Optional

# شبیه‌سازی یک دیتابیس ساده برای ذخیره‌ی کاربران در حافظه (برای تست)
users_db = {}

def handle_text_message(chat_id: int, text: str) -> str:
    """
    مدیریت پیام‌های متنی کاربر و ساخت پاسخ مناسب.
    """
    user = users_db.get(chat_id)

    if not user:
        # ثبت اولین ورود کاربر و درخواست اسم
        users_db[chat_id] = {"step": "ask_name"}
        return "سلام! لطفاً اسم کاملت رو بگو 🤝"

    if user["step"] == "ask_name":
        # ذخیره اسم و پرسیدن مرحله بعدی
        users_db[chat_id]["name"] = text
        users_db[chat_id]["step"] = "main_menu"
        return f"خیلی خوشحال شدم {text} عزیز! 😊\nچه کمکی ازم برمیاد؟ مثلاً: اضافه کردن مشتری 📇 یا دریافت گزارش 📊"

    if user["step"] == "main_menu":
        if "مشتری" in text:
            users_db[chat_id]["step"] = "add_customer_name"
            return "اسم مشتری جدید رو وارد کن 📛"
        elif "گزارش" in text:
            return "هنوز گزارشی آماده نیست 📄 ولی به‌زودی اضافه میشه!"
        else:
            return "متوجه منظورت نشدم 😅 لطفاً یکی از گزینه‌ها رو تایپ کن: مشتری یا گزارش."

    if user["step"] == "add_customer_name":
        users_db[chat_id]["new_customer"] = {"name": text}
        users_db[chat_id]["step"] = "add_customer_phone"
        return "شماره تماس مشتری رو وارد کن ☎️"

    if user["step"] == "add_customer_phone":
        users_db[chat_id]["new_customer"]["phone"] = text
        customer = users_db[chat_id].pop("new_customer")
        users_db[chat_id]["step"] = "main_menu"
        return f"مشتری {customer['name']} با شماره {customer['phone']} با موفقیت ذخیره شد! ✅"

    return "برای شروع مجدد بنویس: شروع"
