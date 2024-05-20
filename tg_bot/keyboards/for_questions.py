from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Новая заявка")
    kb.button(text="Повторить заявку")
    kb.button(text="Мои заявки")
    kb.button(text="Мои юр. лица")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
