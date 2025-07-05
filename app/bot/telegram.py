from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

router = Router()
dp.include_router(router)

# استارت اولیه
@router.message(commands=["start"])
async def start_handler(message: Message, state: FSMContext):
    await message.answer("سلام! خوش اومدی به سیستم مدیریت مشتری 😊\nاسمت چیه؟")
    await state.set_state(UserForm.ask_name)

class UserForm(StatesGroup):
    ask_name = State()
    ask_help = State()

# گرفتن نام
@router.message(UserForm.ask_name)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"خیلی خوب {message.text} عزیز 👌\nچطور می‌تونم کمکت کنم؟")
    await state.set_state(UserForm.ask_help)

# گرفتن درخواست بعدی
@router.message(UserForm.ask_help)
async def help_handler(message: Message, state: FSMContext):
    await message.answer("در حال آماده‌سازی درخواست شما هستم...")
    # در آینده با دیتابیس و مدیریت فروشنده اتصال پیدا خواهد کرد
