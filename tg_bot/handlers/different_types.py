from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(~F.text)
async def handle_non_text_messages(message: Message):
    await message.answer("Извините, но бот понимает только текст, напишите нам пожалуйста!")
