import logging

from aiogram import Bot
from constants import (
    SERVICE_TELEGRAM_TOKEN,
    SERVICE_CHAT_ID,
    TECH_MESSAGES,
)
from requests import get_company_name

service_bot = Bot(token=SERVICE_TELEGRAM_TOKEN)


async def send_message(user_id, text):
    await service_bot.send_message(user_id, text)


async def get_dadata_company_name(inn):
    company_data = await get_company_name(inn)
    company_name = company_data["suggestions"][0]["value"]
    if not company_name:
        await send_message(SERVICE_CHAT_ID, TECH_MESSAGES["company_error"])
        logging.info(TECH_MESSAGES["company_error"])
    return company_name
