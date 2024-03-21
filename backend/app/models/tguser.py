from sqlalchemy import Column, Integer, String

from backend.constants import (
    TG_USERNAME_MAX_LEN,
)
from backend.app.core.db import Base


class TgUser(Base):
    """Модель телеграм-пользователя."""
    tg_id: int = Column(
        Integer,
    )
    tg_username = Column(
        String(TG_USERNAME_MAX_LEN),
        unique=True,
        nullable=False,
    )
    name = Column(String(TG_USERNAME_MAX_LEN))
    lastname = Column(String(TG_USERNAME_MAX_LEN))
