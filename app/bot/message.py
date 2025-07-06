from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def handle_message(message: Message):
    await message.answer("پیام شما دریافت شد.")
