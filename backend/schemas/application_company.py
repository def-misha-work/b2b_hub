from pydantic import BaseModel, Extra, Field


class ApplicationCompanyBase(BaseModel):
    """Базовая схема связи заявка - ИНН компании."""
    company_inn: int = Field(
        ...,
        description="ИНН компании",
    )
    id_application: int

    class Config:
        extra = Extra.forbid


class ApplicationCompanyCreate(ApplicationCompanyBase):
    """Схема для создания связи заявка - ИНН компании."""
    ...


class ApplicationCompanyDB(ApplicationCompanyCreate):
    """Схема связи заявка - ИНН компании."""
    id: int

    class Config:
        orm_mode = True
