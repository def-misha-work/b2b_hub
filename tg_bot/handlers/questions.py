import logging

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from keyboards.for_questions import get_menu
from requests import make_post_request, make_get_request
from storage import UserStorage, ApplicationStorage
from utils import send_message
from validators import validate_date
from constants import (
    MESSAGES, ENDPONT_CREATE_USER, SERVICE_CHAT_ID, ENDPONT_CREATE_APPLICATION, MESSAGES_TO_MANAGER, ENDPONT_GET_APPLICATION_LIST,
)


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

    tg_id = message.from_user.id
    tg_username = message.from_user.username
    tg_name = message.from_user.first_name
    tg_surname = message.from_user.last_name
    user_storage = UserStorage(tg_id, tg_username, tg_name, tg_surname)
    user_dict = user_storage.to_dict()

    try:
        response = await make_post_request(ENDPONT_CREATE_USER, user_dict)
        if response.status_code != 200:
            logging.info(f"Пользователь не создан: {response.status_code}")
            await send_message(SERVICE_CHAT_ID, "Пользователь не создан")
        logging.info("Пользователь создан")
        # await send_message(SERVICE_CHAT_ID, "Пользователь создан") TODO Раскомментировать на бой. # noqa
        # await send_message(SERVICE_CHAT_ID, "Пользователь создан") TODO Сделать отправку Боре. # noqa
    except Exception as e:
        logging.info(f"Ошибка при создании пользователя: {e}")
        await send_message(SERVICE_CHAT_ID, "Ошибка создания пользователя")

    await message.answer(MESSAGES["start"].format(tg_name))
    await message.answer(MESSAGES["menu"], reply_markup=get_menu())
    logging.info("Пользователь в меню")


# Старт цепочки создание заявки step_1
@router.message(StateFilter(None), F.text.lower() == "новая заявка")
async def application_step_one(message: Message, state: FSMContext):
    """Обрабатывает клик по кнопке и запускает цепочку Новая заявка."""
    application_storage.update_tg_id(message.from_user.id)
    await message.answer(MESSAGES["step1"])
    await state.set_state(NewApplication.step_1)
    logging.info("Начато создание новой заявки")


# Обработка inn_payer step_1
@router.message(
    lambda message: message.text.isdigit() and len(message.text) == 10,
    NewApplication.step_1
)
async def get_inn_payer(message: types.Message, state: FSMContext):
    """Обработка сообщения с числом из ровно 10 символов."""
    inn_payer = message.text
    application_storage.update_inn_payer(inn_payer)
    await message.answer(f"Вы ввели ИНН плательщика: {inn_payer}")
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
    inn_recipient = message.text
    application_storage.update_inn_recipient(inn_recipient)
    await message.answer(f"Вы ввели ИНН получателя: {inn_recipient}")
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
    application_cost = message.text
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
    """Валидация сообщения с числом из 12 символов."""
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
    application_info = MESSAGES["application"].format(
        application_storage.inn_payer,
        application_storage.inn_recipient,
        application_storage.application_cost,
        application_storage.target_date
    )
    logging.info("Успех шаг 4")

    application_dict = application_storage.to_dict()
    try:
        response = await make_post_request(
            ENDPONT_CREATE_APPLICATION, application_dict
        )
        if response.status_code != 201:
            logging.info(f"Заявка не создана БД: {response.status_code}")
            await send_message(SERVICE_CHAT_ID, "Заявка не создана БД")
        logging.info("Заявка создана в БД")
        # Отправляем в саппорт
        application_to_manager = MESSAGES_TO_MANAGER["application_created"].format(
            message.from_user.first_name,
            message.from_user.username,
            application_info
        )
        await send_message(SERVICE_CHAT_ID, application_to_manager)
        logging.info("Заявка отправлена в саппорт")
        # Отправляем менеджеру
        # await send_message(MANAGER_CHAT_ID, application_to_manager) TODO Расскоментить на бою. # noqa
        # logging.info("Заявка отправлена менеджеру")
    except Exception as e:
        logging.info(f"Ошибка при создании заявки: {e}")
        await send_message(SERVICE_CHAT_ID, "Ошибка создания заявки")

    await message.answer("Ваша заявка:" + application_info)
    await message.answer(MESSAGES["application_created"])
    await state.set_state(None)
    await message.answer(MESSAGES["menu"], reply_markup=get_menu())
    logging.info("Пользователь в меню")


@router.message(F.text, NewApplication.step_4)
async def invalid_values_target_date(
    message: types.Message,
    state: FSMContext
):
    """Валидация даты."""
    await message.answer("Внимание! Дата должна быть в формате: 20.10.25, и не ранее текущего дня.")
    await message.answer(MESSAGES["step4"])
    await state.set_state(NewApplication.step_4)
    logging.info("Ошибка на шаге 4")


@router.message(F.text.lower() == "мои заявки")
async def answer_no(message: Message):
    """Обрабатывает клик по кнопке."""
    tg_id = message.from_user.id
    response = await make_get_request(ENDPONT_GET_APPLICATION_LIST, tg_id)
    print(response.status_code)
    print(response.text)
    await message.answer("Ваши заявки: " + response.text)
    logging.info("Пользователь запросил заявки")


@router.message(F.text.lower() == "мои юр. лица")
async def answer_no1(message: Message):
    """Обрабатывает клик по кнопке."""
    tg_id = message.from_user.id
    response = await make_get_request(ENDPONT_GET_APPLICATION_LIST, tg_id)
    await message.answer("Ваши юр. лица: " + response.text) # TODO Получить по api название компании
    logging.info("Пользователь запросил юр. лица")
