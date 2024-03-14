
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text

from backend.constants import (
    CREATE_DATE_DEFAULT, COMPANY_NAME_MAX_LEN,
    COMPANY_ID_FOREIGN_KEY, COMPANY_INN_FOREIGN_KEY,
)
from backend.app.core.db import Base


class Company(Base):
    """Модель компании."""
    company_name = Column(
        String(COMPANY_NAME_MAX_LEN),
        ForeignKey(COMPANY_ID_FOREIGN_KEY),
        unique=False,  # а вот уникальное ли?
        nullable=False,  # подтянем при развитии проекта
    )
    company_inn = Column(
        Integer,
        ForeignKey(COMPANY_INN_FOREIGN_KEY),
        unique=True,
    )
    company_add_date = Column(
        DateTime,
        default=CREATE_DATE_DEFAULT,
    )
    # user - тот кто добавил??
