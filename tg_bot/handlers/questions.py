import logging

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.for_questions import get_menu
from requests import make_post_request
from storage import UserStorage, ApplicationStorage
from utils import send_message
from constants import MESSAGES, ENDPONT_CREATE_USER, SERVICE_CHAT_ID


router = Router()
appl_storage = ApplicationStorage()


class NewApplication(StatesGroup):
    step_1 = State()
    step_2 = State()
    step_3 = State()
    step_4 = State()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    """Запускает бота по команде /start. Выводит меню.
    Отправляет в БД запрос на создание юзера."""
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


# Старт цепочки создание заявки step_1
@router.message(StateFilter(None), F.text.lower() == "новая заявка")
async def application_step_one(message: Message, state: FSMContext):
    """Обрабатывает клик по кнопке и запускает цепочку Новая заявка."""
    await message.answer(MESSAGES["step1"])
    await state.set_state(NewApplication.step_1)


# Обработка inn_payer step_1
@router.message(
    lambda message: message.text.isdigit() and len(message.text) == 10,
    NewApplication.step_1
)
async def get_inn_payer(message: types.Message, state: FSMContext):
    """Обработка сообщения с числом из ровно 10 символов."""
    number = message.text
    await message.answer(f"Вы ввели ИНН плательщика: {number}")
    await message.answer(MESSAGES["step2"])
    await state.set_state(NewApplication.step_2)


@router.message(F.text, NewApplication.step_1)
async def invalid_values_inn_payer(message: types.Message, state: FSMContext):
    """Валидация сообщения с числом из 10 символов."""
    await message.answer("Внимание! ИНН организации должен содержать 10 цифр!")
    await message.answer(MESSAGES["step1"])
    await state.set_state(NewApplication.step_1)


# Обработка inn_recipient step_2
@router.message(
    lambda message: message.text.isdigit() and len(message.text) == 12,
    NewApplication.step_2
)
async def get_inn_recipient(message: types.Message, state: FSMContext):
    """Обработка сообщения с числом из ровно 12 символов."""
    number = message.text
    await message.answer(f"Вы ввели ИНН получателя: {number}")
    await message.answer(MESSAGES["step3"])
    await state.set_state(NewApplication.step_3)


@router.message(F.text, NewApplication.step_2)
async def invalid_values_inn_recipient(message: types.Message, state: FSMContext):
    """Валидация сообщения с числом из 12 символов."""
    await message.answer("Внимание! ИНН ИП должен содержать 12 цифр!")
    await message.answer(MESSAGES["step2"])
    await state.set_state(NewApplication.step_2)


# Обработка application_cost step_3
@router.message(
    lambda message: message.text.isdigit(),
    NewApplication.step_3
)
async def get_application_cost(message: types.Message, state: FSMContext):
    """Обработка сообщения с числом."""
    number = message.text
    await message.answer(f"Вы ввели сумму заявки: {number}")
    await message.answer(MESSAGES["step4"])
    await state.set_state(NewApplication.step_4)


@router.message(F.text, NewApplication.step_3)
async def invalid_values_application_cost(message: types.Message, state: FSMContext):
    """Валидация сообщения с числом из 12 символов."""
    await message.answer("Внимание! Сумма должна быть числом!")
    await message.answer(MESSAGES["step3"])
    await state.set_state(NewApplication.step_3)


@router.message(F.text.lower() == "мои заявки")
async def answer_no(message: Message):
    """Обрабатывает клик по кнопке."""
    await message.answer("Жаль\\.\\.\\.")


@router.message(F.text.lower() == "мои юр. лица")
async def answer_no1(message: Message):
    """Обрабатывает клик по кнопке."""
    await message.answer("Чтото\\.\\.\\.")
