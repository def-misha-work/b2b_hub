from sqlalchemy import Column, DateTime, Integer, String

from backend.constants import (
    CREATE_DATE_DEFAULT, COMPANY_NAME_MAX_LEN,
)
from backend.app.core.db import Base


class Company(Base):
    """Модель для компаний (плательщиков и получателей)."""
    company_name = Column(
        String(COMPANY_NAME_MAX_LEN),
        unique=False,  # а вот уникальное ли?
        nullable=True,  # подтянем при развитии проекта
    )
    company_inn = Column(Integer, unique=True)
    company_add_date = Column(DateTime, default=CREATE_DATE_DEFAULT)
    # user_id = Column(Integer, ForeignKey('user.id'))
