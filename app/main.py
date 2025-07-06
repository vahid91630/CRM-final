import asyncio
from aiogram import Bot, Dispatcher
from app.config import settings
from app.bot.handlers import message

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(message.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
