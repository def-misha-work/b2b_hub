import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import questions, different_types
from constants import TELEGRAM_TOKEN


logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode="MarkdownV2")
    dp = Dispatcher()
    dp.include_router(questions.router)
    dp.include_router(different_types.router)
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
