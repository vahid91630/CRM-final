from aiogram import types

async def start_handler(message: types.Message):
    await message.reply("سلام! به ربات CRM خوش آمدید.")
