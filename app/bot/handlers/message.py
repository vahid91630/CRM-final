from aiogram import Router, types
from aiogram.types import Message

router = Router()

@router.message()
async def handle_message(message: Message):
    await message.answer("درخواست شما دریافت شد.")
