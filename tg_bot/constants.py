import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SERVICE_TELEGRAM_TOKEN = os.getenv("SERVICE_TELEGRAM_TOKEN")
SERVICE_CHAT_ID = os.getenv("SERVICE_CHAT_ID")
MANAGER_CHAT_ID = os.getenv("MANAGER_CHAT_ID")

# ENDPONT_CREATE_USER = "https://webhook.site/d08effda-18c1-4e76-be8e-990b27c72eca" # noqa
# ENDPONT_CREATE_APPLICATION = "https://webhook.site/d08effda-18c1-4e76-be8e-990b27c72eca" # noqa
# ENDPONT_GET_APPLICATION_LIST = "https://webhook.site/d08effda-18c1-4e76-be8e-990b27c72eca" # noqa
ENDPONT_CREATE_USER = "http://backend:8000/tguser/"
ENDPONT_CREATE_APPLICATION = "http://backend:8000/application/"
ENDPONT_GET_APPLICATION_LIST = "http://backend:8000/application/my/"
ENDPONT_GET_COMPANY_LIST = "http://backend:8000/company/my/"
ENDPONT_PATCH_COMPANY = "http://backend:8000/company/"
ENDPONT_GET_COMPANY_NAME = "http://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party" # noqa
DADATA_API_KEY = "c132632530b566d1a154c8379ce78e6d6b1c9713"

BASIC_USER_LOGIN = os.getenv("BASIC_USER_LOGIN")
BASIC_USER_PASSWORD = os.getenv("BASIC_USER_PASSWORD")

start_message = "Добрый день, {}!\nСервис B2Bhub приветствует Вас!"
menu_message = "Это Меню, выберите что Вы хотите сделать:"
step1_message = """
Шаг 1 из 4:
\nСоздание новой заявки:
\nУкажите ИНН вашей организации, кто будет плательщиком.
"""
step2_message = "Шаг 2 из 4:\nУкажите ИНН вашего ИП, кто будет получателем."
step3_message = """
Шаг 3 из 4:
\nВведите сумму заявки в рублях без указания валюты и без пробелов.
\nНапример: 100000 или 1000000.
"""
step4_message = """
Шаг 4 из 4:
\nВведите дату к которой заявку нужно выполнить, в формате: дд.мм.гг.
\nНапример: '20.10.25' или '20.10.2025'
"""
application_message = """
Номер заявки: {},
\nИНН плательщика: {},
\nНаименование плательщика: {},
\nИНН получателя: {},
\nНаименование получателя: {},
\nСумма заявки: {},
\nДата выполнения заявки: {}
"""
application_created_message = """
Ваша заявка создана:
\nМы свяжемся в Вами в ближайшее рабочее время. Спасибо!
"""
company_message = "Название компании: {}\nИНН компании: {}"


MESSAGES = {
    "start": start_message,
    "menu": menu_message,
    "step1": step1_message,
    "step2": step2_message,
    "step3": step3_message,
    "step4": step4_message,
    "application": application_message,
    "application_created": application_created_message,
    "company": company_message,
}

MESSAGES_TO_MANAGER = {
    "application_created": "Заявка от пользователя: {},\nНик в TG: @{}\nЗаявка: {}",
}
TECH_MESSAGES = {
    "alert_message": "Извините, но я могу обработать только текст",
    "api_error": "Извините произошла ошибка, попробуйте еще раз через пару минут. Администратор уже получил уведомление о ошибке.",
    "company_error": "Не удалось получить названия компании по ИНН",
}
