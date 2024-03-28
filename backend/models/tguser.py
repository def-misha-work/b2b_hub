from sqlalchemy import Column, BigInteger, String

from constants import (
    TG_USERNAME_MAX_LEN,
)
from core.db import Base


class TgUser(Base):
    """Модель телеграм-пользователя."""
    tg_user_id: int = Column(BigInteger, unique=True)
    tg_username = Column(
        String(TG_USERNAME_MAX_LEN),
        unique=True,
        nullable=False,
    )
    name = Column(String(TG_USERNAME_MAX_LEN), nullable=True)
    lastname = Column(String(TG_USERNAME_MAX_LEN), nullable=True)
