import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SERVICE_TELEGRAM_TOKEN = os.getenv("SERVICE_TELEGRAM_TOKEN")
SERVICE_CHAT_ID = os.getenv("SERVICE_CHAT_ID")

ENDPONT_CREATE_USER = "https://webhook.site/d08effda-18c1-4e76-be8e-990b27c72eca" # noqa
# ENDPONT_CREATE_USER = "https://ya.ru/"

MESSAGES = {
    "start": "Добрый день, {}!\nСервис B2Bhub приветствует Вас!",
    "menu": "Вы в меню выберите что вы хотите сделать:",
    "step1": "Шаг 1 из 4:\nСоздание новой заявки:\nУкажите ИНН вашей организации, кто будет плательщиком.", # noqa
    "step2": "Шаг 2 из 4:\nУкажите ИНН вашего ИП, кто будет получателем.", # noqa
    "step3": "Шаг 3 из 4:\nВведите сумму заявки в рублях без указания валюты и без пробелов.\nНапример: 100000 или 1000000.", # noqa
    "step4": "Шаг 4 из 4:\nВведите дату к которой заявку нужно выполнить, в формате: дд.мм.гг.\nНапример: 20.10.25", # noqa
}
TECH_MESSAGES = {
    "alert_message": "Извините, но я могу обработать только текст",
}
