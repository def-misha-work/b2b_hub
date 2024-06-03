import logging
import json

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

from keyboards.for_questions import get_menu
from requests import (
    make_post_request,
    make_get_request,
    make_patch_request,
)
from storage import UserStorage, ApplicationStorage
from utils import send_message, get_dadata_company_name
from validators import validate_date
from constants import (
    MESSAGES,
    TECH_MESSAGES,
    ENDPONT_CREATE_USER,
    SERVICE_CHAT_ID,
    ENDPONT_CREATE_APPLICATION,
    MESSAGES_TO_MANAGER,
    ENDPONT_GET_APPLICATION_LIST,
    ENDPONT_GET_COMPANY_LIST,
    ENDPONT_PATCH_COMPANY,
    MANAGER_CHAT_ID
)


load_dotenv()
router = Router()
application_storage = ApplicationStorage()


class NewApplication(StatesGroup):
    step_1 = State()
    step_2 = State()
    step_3 = State()
    step_4 = State()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    """Запускает бота по команде /start. Выводит меню.
    Отправляет в БД запрос на создание юзера."""
    logging.info("Пользователь запустил бота")
    await state.set_state(None)

    tg_id = str(message.from_user.id)
    tg_username = message.from_user.username
    tg_name = message.from_user.first_name
    tg_surname = message.from_user.last_name
    user_storage = UserStorage(tg_id, tg_username, tg_name, tg_surname)
    user_dict = user_storage.to_dict()

    try:
        response = await make_post_request(ENDPONT_CREATE_USER, user_dict)
        if response.status_code == 200:
            logging.info(f"""
                Пользователь уже есть:  @{tg_username},
                код: {response.status_code}""")
        elif response.status_code == 201:
            logging.info(f"Пользователь создан @{tg_username}")
            await send_message(
                SERVICE_CHAT_ID, f"Новый пользователь @{tg_username}"
            )
            await send_message(
                MANAGER_CHAT_ID, f"Новый пользователь @{tg_username}"
            )
        else:
            logging.info(f"Пользователь не создан: {response.status_code}")
            await send_message(
                SERVICE_CHAT_ID, f"Пользователь не создан @{tg_username}"
            )
    except Exception as e:
        logging.info(f"Ошибка при создании пользователя: {e}")
        await send_message(SERVICE_CHAT_ID, "Ошибка создания пользователя")

    await message.answer(MESSAGES["start"].format(tg_name))
    await message.answer(MESSAGES["menu"], reply_markup=get_menu())
    logging.info(f"Пользователь @{tg_username} в меню")


# Старт цепочки создание заявки step_1
@router.message(StateFilter(None), F.text.lower() == "новая заявка")
async def application_step_one(message: Message, state: FSMContext):
    """Обрабатывает клик по кнопке и запускает цепочку Новая заявка."""

    tg_username = message.from_user.username
    application_storage.update_tg_id(message.from_user.id)
    await message.answer(MESSAGES["step1"])
    await state.set_state(NewApplication.step_1)
    logging.info(f"@{tg_username} начал создание новой заявки")


# Обработка inn_payer step_1
@router.message(
    lambda message: message.text.isdigit() and len(message.text) == 10,
    NewApplication.step_1
)
async def get_inn_payer(message: types.Message, state: FSMContext):
    """Обработка сообщения с числом из ровно 10 символов."""
    inn_payer = int(message.text)
    application_storage.update_inn_payer([inn_payer])
    await message.answer(f"Вы ввели ИНН плательщика: {inn_payer}")

    # получаем и сохраняем данные компании
    try:
        company_name = await get_dadata_company_name(inn_payer)
        application_storage.update_name_payer(company_name)
        await message.answer(f"Название вашей компании: {company_name}")
    except Exception:
        await message.answer(TECH_MESSAGES["company_error"])

    # Обновляем информацию о компаниях в базе.
    company_patch_url = f"""
            {ENDPONT_PATCH_COMPANY}{application_storage.inn_payer}/update
            """
    data = {
        "company_inn": application_storage.inn_payer,
        "company_name": application_storage.name_payer,
        }
    try:
        await make_patch_request(
            company_patch_url,
            data,
        )
    except Exception as e:
        logging.info(f"Ошибка {e} запроса обновления компании")

    await message.answer(MESSAGES["step2"])
    await state.set_state(NewApplication.step_2)
    logging.info("Успех шаг 1")


@router.message(F.text, NewApplication.step_1)
async def invalid_values_inn_payer(message: types.Message, state: FSMContext):
    """Валидация сообщения с числом из 10 символов."""
    await message.answer("Внимание! ИНН организации должен содержать 10 цифр!")
    await message.answer(MESSAGES["step1"])
    await state.set_state(NewApplication.step_1)
    logging.info("Ошибка на шаге 1")


# Обработка inn_recipient step_2
@router.message(
    lambda message: message.text.isdigit() and len(message.text) == 12,
    NewApplication.step_2
)
async def get_inn_recipient(message: types.Message, state: FSMContext):
    """Обработка сообщения с числом из ровно 12 символов."""
    inn_recipient = int(message.text)
    application_storage.update_inn_recipient([inn_recipient])
    await message.answer(f"Вы ввели ИНН получателя: {inn_recipient}")

    # получаем и сохраняем данные компании
    try:
        company_name = await get_dadata_company_name(inn_recipient)
        application_storage.update_name_recipient(company_name)
        await message.answer(f"Название вашей компании: {company_name}")
    except Exception:
        await message.answer(TECH_MESSAGES["company_error"])

    # Обновляем информацию о компаниях в базе.
    company_patch_url = f"""
            {ENDPONT_PATCH_COMPANY}{application_storage.inn_recipient}/update
            """
    data = {
        "company_inn": application_storage.inn_recipient,
        "company_name": application_storage.name_recipient,
        }
    try:
        await make_patch_request(
            company_patch_url,
            data,
        )
    except Exception as e:
        logging.info(f"Ошибка {e} запроса обновления компании")

    await message.answer(MESSAGES["step3"])
    await state.set_state(NewApplication.step_3)
    logging.info("Успех шаг 2")


@router.message(F.text, NewApplication.step_2)
async def invalid_values_inn_recipient(
    message: types.Message,
    state: FSMContext
):
    """Валидация сообщения с числом из 12 символов."""
    await message.answer("Внимание! ИНН ИП должен содержать 12 цифр!")
    await message.answer(MESSAGES["step2"])
    await state.set_state(NewApplication.step_2)
    logging.info("Ошибка на шаге 2")


# Обработка application_cost step_3
@router.message(
    lambda message: message.text.isdigit(),
    NewApplication.step_3
)
async def get_application_cost(message: types.Message, state: FSMContext):
    """Обработка сообщения с суммой заявки."""
    application_cost = int(message.text)
    application_storage.update_application_cost(application_cost)
    await message.answer(f"Вы ввели сумму заявки: {application_cost}")
    await message.answer(MESSAGES["step4"])
    await state.set_state(NewApplication.step_4)
    logging.info("Успех шаг 3")


@router.message(F.text, NewApplication.step_3)
async def invalid_values_application_cost(
    message: types.Message,
    state: FSMContext
):
    """Валидация сообщения с суммаой заявки."""
    await message.answer("Внимание! Сумма должна быть числом!")
    await message.answer(MESSAGES["step3"])
    await state.set_state(NewApplication.step_3)
    logging.info("Ошибка на шаге 3")


# Обработка target_date step_4
@router.message(
    lambda message: validate_date(message.text),
    NewApplication.step_4
)
async def get_target_date(message: types.Message, state: FSMContext):
    """Обработка сообщения с датой в формате 20.10.25."""
    target_date = message.text
    application_storage.update_target_date(target_date)
    tg_username = message.from_user.username

    application_dict = application_storage.to_dict()
    # TODO убрать костыль после доработки бека.
    del application_dict['name_payer']
    del application_dict['name_recipient']
    
    application_id = False
    try:
        response = await make_post_request(
            ENDPONT_CREATE_APPLICATION, application_dict
        )
        data = json.loads(response.text)
        application_id = data["id"]
    except Exception as e:
        logging.info(f"Ошибка при создании заявки: {e}")
        await send_message(SERVICE_CHAT_ID, f"Ошибка создания заявки {e}")
        await message.answer(TECH_MESSAGES["api_error"])

    # Отправляем в саппорт
    if application_id:
        application_storage.update_application_id(application_id)
        application_info = MESSAGES["application"].format(
            application_storage.application_id,
            *application_storage.inn_payer,
            application_storage.name_payer,
            *application_storage.inn_recipient,
            application_storage.name_recipient,
            application_storage.application_cost,
            application_storage.target_date
        )
        application_to_manager = MESSAGES_TO_MANAGER["application_created"].format(
            message.from_user.first_name,
            message.from_user.username,
            application_info
        )
        await send_message(SERVICE_CHAT_ID, application_to_manager)
        await send_message(MANAGER_CHAT_ID, application_to_manager)
        await message.answer("Ваша заявка:" + application_info)
        await message.answer(MESSAGES["application_created"])
        await state.set_state(None)
        await message.answer(MESSAGES["menu"], reply_markup=get_menu())
        logging.info(f"Пользователь {tg_username} в меню")
        logging.info("Успех шаг 4")


@router.message(F.text, NewApplication.step_4)
async def invalid_values_target_date(
    message: types.Message,
    state: FSMContext
):
    """Валидация даты."""
    await message.answer(
        "Введите дату в формате: 20.10.25, не ранее текущего дня."
    )
    await message.answer(MESSAGES["step4"])
    await state.set_state(NewApplication.step_4)
    logging.info("Ошибка на шаге 4")


@router.message(F.text.lower() == "мои заявки")
async def get_application_list(message: Message):
    """Обрабатывает клик по кнопке Список заявок."""
    tg_id = str(message.from_user.id)
    application_list = False
    try:
        response = await make_get_request(ENDPONT_GET_APPLICATION_LIST, tg_id)
        application_list = json.loads(response.text)
    except Exception as e:
        logging.info(f"Ошибка при получение спиcка заявок: {e}")
        await send_message(
            SERVICE_CHAT_ID, f"Ошибка при получение спика заявок: {e}"
        )
        await message.answer(TECH_MESSAGES["api_error"])

    if application_list:
        for application in application_list:
            answer = MESSAGES["application"].format(
                application["id"],
                *application["inn_payer"],
                # application["name_payer"],
                *application["inn_recipient"],
                # application["name_recipient"],
                application["cost"],
                application["target_date"],
            )
            await message.answer(f"Ваши заявки: {answer}")
        logging.info("Пользователь получил список заявок")

        await message.answer(MESSAGES["menu"], reply_markup=get_menu())
        logging.info("Пользователь в меню")
    else:
        await message.answer("У вас нет активных заявок.")
        logging.info("Пользователь получил список заявок (пустой)")
    await message.answer(MESSAGES["menu"], reply_markup=get_menu())
    logging.info("Пользователь в меню")


@router.message(F.text.lower() == "мои юр. лица")
async def answer_no1(message: Message):
    """Обрабатывает клик по кнопке 'мои юр. лица'."""
    logging.info("Пользователь запросил компании")
    tg_id = str(message.from_user.id)
    company_list = False
    try:
        response = await make_get_request(ENDPONT_GET_COMPANY_LIST, tg_id)
        company_list = json.loads(response.text)
    except Exception as e:
        logging.info(f"Ошибка при получение спиcка компаний: {e}")
        await send_message(
            SERVICE_CHAT_ID, f"Ошибка при получение спиcка компаний: {e}"
        )
        await message.answer(TECH_MESSAGES["api_error"])

    if company_list:
        for company in company_list:
            answer = MESSAGES["company"].format(
                company["company_name"],
                company["company_inn"]
            )
            await message.answer(answer)
        logging.info("Пользователь получил список компаний")
    else:
        await message.answer(
            "Создайте первую заявку, для добавления компании."
        )
        logging.info("Пользователь получил список заявок (пустой)")

    await message.answer(MESSAGES["menu"], reply_markup=get_menu())
    logging.info("Пользователь в меню")


@router.message(StateFilter(None), F.text.lower() == "повторить заявку")
async def application_repeat(message: Message, state: FSMContext):
    """Обрабатывает клик по кнопке Повторить заявку."""
    tg_id = str(message.from_user.id)
    try:
        response = await make_get_request(ENDPONT_GET_APPLICATION_LIST, tg_id)
    except Exception as e:
        logging.info(f"Ошибка при получение спиcка заявок: {e}")
        await send_message(
            SERVICE_CHAT_ID, f"Ошибка при получение спика заявок: {e}"
        )
        await message.answer(TECH_MESSAGES["api_error"])
    logging.info(f"Ответ с заявками {response.text}")
    logging.info(f"Ответ с заявками {type(response.text)}")
    last_application = json.loads(response.text)
    await message.answer(f"Ваша последняя заявка: {last_application[-1]}")
