from aiogram import Bot, Dispatcher
from app.bot.handlers import start_handler
from app.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start_handler, commands=["start"])
