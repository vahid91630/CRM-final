from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("سلام 👋 به CRM خوش اومدی!\nبرای استفاده از امکانات ربات از دکمه‌ها یا دستورات استفاده کن.")
