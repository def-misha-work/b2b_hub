from sqlalchemy import Column, DateTime, ForeignKey, BigInteger, String

from constants import (
    CREATE_DATE_DEFAULT, COMPANY_NAME_MAX_LEN, TG_USER_FOREIGN_KEY,
)
from core.db import Base


class Company(Base):
    """Модель для компаний (плательщиков и получателей)."""
    company_name = Column(
        String(COMPANY_NAME_MAX_LEN),
        unique=False,  # а вот уникальное ли?
        nullable=True,  # подтянем при развитии проекта
    )
    company_inn = Column(BigInteger, unique=True)
    company_add_date = Column(DateTime, default=CREATE_DATE_DEFAULT)
    tg_user_id = Column(BigInteger, ForeignKey(TG_USER_FOREIGN_KEY))
