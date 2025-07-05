from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from config import settings

bot = Bot(token=settings.bot_token, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)
