from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text

from backend.constants import (
    CREATE_DATE_DEFAULT,
    COMPANY_ID_FOREIGN_KEY, COMPANY_INN_FOREIGN_KEY,
)
from backend.app.core.db import Base


class Application(Base):
    """Модель заявки."""
    # будет подставляться на этапе endpoints
    company_id = Column(
        Integer,
        ForeignKey(COMPANY_ID_FOREIGN_KEY),
        unique=False,
        nullable=False,
    )
    inn = Column(
        Integer,
        ForeignKey(COMPANY_INN_FOREIGN_KEY),
        unique=True,
    )
    created = Column(
        DateTime,
        default=CREATE_DATE_DEFAULT,
    )
    target_date = Column(
        DateTime,
        nullable=False,
    )
    cost = Column(
        Float,
        nullable=False,
    )
