from aiogram import types
from app.bot.telegram import dp

@dp.message_handler(commands=['start', 'سلام'])
async def start_handler(message: types.Message):
    await message.answer("سلام 👋 من دستیار CRM شما هستم. چطور می‌تونم کمکتون کنم؟")
