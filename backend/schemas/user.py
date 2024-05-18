from typing import Optional

from pydantic import BaseModel, Extra, Field


class UserBase(BaseModel):
    """Базовая схема пользователя."""
    username: str = Field(
        ...,
        description="Username пользователя",
    )
    password: str

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    """Схема для обновления полей пользователя."""
    ...


class UserDB(UserBase):
    """Схема пользователя в БД."""
    id: int = Field(
        ...,
        primary_key=True,
        description="id пользователя",
    )
    is_superuser: bool = False

    class Config:
        orm_mode = True
