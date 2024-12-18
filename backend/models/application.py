from sqlalchemy import Column, DateTime, Float, ForeignKey, BigInteger, String

from constants import (
    CREATE_DATE_DEFAULT, TG_USER_FOREIGN_KEY,
)
from core.db import Base


class Application(Base):
    """Модель заявки."""
    create_date = Column(
        DateTime,
        default=lambda: CREATE_DATE_DEFAULT,
    )
    # Ожидаемая дата выполнения заявки, например 27.03.2024
    target_date = Column(
        String,
        nullable=False,
    )
    cost = Column(
        Float,
        nullable=False,
    )
    tg_user_id = Column(BigInteger, ForeignKey(TG_USER_FOREIGN_KEY))
