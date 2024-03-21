from datetime import datetime
from typing import List

from pydantic import BaseModel, Extra, Field, validator

from backend.constants import CREATE_DATE, EMPTY_FIELD_ERROR


class ApplicationBase(BaseModel):
    """Базовая схема заявки."""
    target_date: datetime = Field(
        ...,
        example=CREATE_DATE,
        description="Ожидаемая дата выполнения заявки",
    )
    cost: float = Field(
        ...,
        description="Сумма заявки",
    )

    class Config:
        extra = Extra.forbid


class ApplicationCreate(ApplicationBase):
    """Схема для создания заявки."""
    inn_payer: List[int] = Field(
        ...,
        description="Список ИНН плательщиков",
    )
    inn_recipient: List[int] = Field(
        ...,
        description="Список ИНН получателей",
    )


class ApplicationUpdate(ApplicationCreate):
    """Схема для обновления полей заявки."""

    @validator('inn_payer', 'inn_recipient', 'target_date', 'cost')
    def field_cannot_be_null(cls, value, field):
        if value is None:
            raise ValueError(EMPTY_FIELD_ERROR.format(field.name))
        return value


class ApplicationDB(ApplicationCreate):
    """Схема заявки в БД."""
    id: int
    create_date: datetime = Field(
        ...,
        example=CREATE_DATE,
        description="Дата создания заявки",
    )

    class Config:
        orm_mode = True


class ApplicationResponse(ApplicationCreate):
    """Схема заявки в БД."""
    id: int

    class Config:
        orm_mode = True