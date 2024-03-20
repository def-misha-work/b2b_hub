from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.for_questions import get_menu
from constants import MESSAGES

router = Router()  # [1]


class NewApplication(StatesGroup):
    inn_payer = State()
    inn_recipient = State()
    inn_recipient = State()
    inn_date = State()


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    fullname = message.from_user.full_name
    await message.answer(
        MESSAGES["start"].format(fullname),
        reply_markup=get_menu()
    )


@router.message(StateFilter(None), F.text.lower() == "новая заявка")
async def application_step_one(message: Message, state: FSMContext):
    await message.answer(MESSAGES["step1"])
    await state.set_state(NewApplication.inn_payer)


@router.message(
    lambda message: message.text.isdigit() and len(message.text) == 10,
    NewApplication.inn_payer
)
async def handle_ten_digit_number(message: types.Message, state: FSMContext):
    # Обработка сообщения с числом из ровно 10 символов
    number = message.text
    await message.answer(f"Вы ввели число из 10 символов: {number}")
    await state.set_state(NewApplication.inn_recipient)


@router.message(F.text.lower() == "мои заявки")
async def answer_no(message: Message):
    await message.answer("Жаль\\.\\.\\.")


@router.message(F.text.lower() == "мои юр. лица")
async def answer_no1(message: Message):
    await message.answer("Чтото\\.\\.\\.")
