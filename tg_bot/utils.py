from aiogram import Bot
from constants import SERVICE_TELEGRAM_TOKEN

service_bot = Bot(token=SERVICE_TELEGRAM_TOKEN)


async def send_message(user_id, text):
    await service_bot.send_message(user_id, text)
