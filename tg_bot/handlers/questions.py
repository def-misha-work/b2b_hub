import json

from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.for_questions import get_menu
from constants import MESSAGES

router = Router()  # [1]


class Storage:
    user_storage = {}
    id = None
    file_name = "storage.json"

    def __init__(self, id):
        if not self.user_storage:
            try:
                self._load()
            except Exception as e:
                print(e)
                self._dump()
        if id and (id in self.user_storage):
            self.id = id
        elif id:
            self.id = id
            self.user_storage[id] = {}

    def _load(self):
        with open(self.file_name, "r") as f:
            self.user_storage = json.loads(f.read())

    def _dump(self):
        with open(self.file_name, "w") as f:
            f.write(json.dumps(self.user_storage))

    def set_val(self, val_name, val):
        self.user_storage[self.id][val_name] = val
        self._dump()

    def get_val(self, val_name):
        return self.user_storage[self.id].get(val_name, None)


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
async def get_inn_payer(message: types.Message, state: FSMContext):
    # Обработка сообщения с числом из ровно 10 символов
    number = message.text
    await message.answer(f"Вы ввели ИНН: {number}")
    await state.set_state(NewApplication.inn_recipient)


@router.message(F.text, NewApplication.inn_payer)
async def invalid_values_inn_payer(message: types.Message, state: FSMContext):
    await message.answer("Внимание\\! ИНН должен содержать 10 цифр\\!")
    await message.answer(MESSAGES["step1"])
    await state.set_state(NewApplication.inn_payer)


@router.message(F.text.lower() == "мои заявки")
async def answer_no(message: Message):
    await message.answer("Жаль\\.\\.\\.")


@router.message(F.text.lower() == "мои юр. лица")
async def answer_no1(message: Message):
    await message.answer("Чтото\\.\\.\\.")
