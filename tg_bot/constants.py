import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


MESSAGES = {
    "start": "Добрый день, {}\\!\nСервис B2Bhub приветствует Вас\\!",
    "menu": "Вы в меню выберите что вы хотите сделать.",
    "step1": "Шаг 1 из 4:\nСоздание новой заявки:\nУкажите ИНН вашей организации, кто будет плательщиком\\." # noqa
}
TECH_MESSAGES = {
    "alert_message": "Извините, но я могу обработать только текст",
}
