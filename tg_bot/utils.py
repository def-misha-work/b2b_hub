from aiogram import Bot
from constants import SERVICE_TELEGRAM_TOKEN
from requests import get_company_name

service_bot = Bot(token=SERVICE_TELEGRAM_TOKEN)


async def send_message(user_id, text):
    await service_bot.send_message(user_id, text)


async def get_dadata_company_name(inn):
    company_data = await get_company_name(inn)
    company_name = company_data["suggestions"][0]["value"]
    return company_name
