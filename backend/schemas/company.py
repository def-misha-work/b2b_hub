from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Extra, Field


class CompanyBase(BaseModel):
    """Базовая схема компании."""
    company_name: Optional[str] = Field(
        None,
        description="Название компании",
    )
    company_inn: int = Field(
        ...,
        description="ИНН компании",
    )
    tg_user_id: int

    class Config:
        extra = Extra.forbid


class CompanyCreate(CompanyBase):
    """Схема для создания компании."""
    ...


class CompanyUpdate(CompanyBase):
    """Схема для обновления полей компании."""
    ...


class CompanyDB(CompanyCreate):
    """Схема компании в БД."""
    id: int
    company_add_date: datetime = Field(
        ...,
        description="Дата добавления компании",
    )

    class Config:
        orm_mode = True
