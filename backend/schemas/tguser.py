from typing import Optional

from pydantic import BaseModel, Extra, Field


class TgUserBase(BaseModel):
    """Базовая схема telegram-пользователя."""
    tg_username: str = Field(
        ...,
        description="Username telegram-пользователя",
    )
    tg_user_id: int = Field(
        ...,
        primary_key=True,
        description="id telegram-пользователя",
    )
    name: Optional[str] = Field(
        None,
        description="Имя telegram-пользователя",
    )
    lastname: Optional[str] = Field(
        None,
        description="Фамилия telegram-пользователя",
    )

    class Config:
        extra = Extra.forbid


class TgUserCreate(TgUserBase):
    """Схема для создания telegram-пользователя."""
    ...


class TgUserUpdate(TgUserBase):
    """Схема для обновления полей telegram-пользователя."""
    ...


class TgUserDB(TgUserCreate):
    """Схема telegram-пользователя в БД."""
    ...

    class Config:
        orm_mode = True
