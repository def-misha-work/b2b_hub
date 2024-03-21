from sqlalchemy import Column, DateTime, Float

from backend.constants import (
    CREATE_DATE_DEFAULT,
)
from backend.app.core.db import Base


class Application(Base):
    """Модель заявки."""
    # Дата создания заявки
    create_date = Column(
        DateTime,
        default=CREATE_DATE_DEFAULT,
    )
    # Ожидаемая дата выполнения заявки
    target_date = Column(
        DateTime,
        nullable=False,
    )
    # Сумма заявки
    cost = Column(
        Float,
        nullable=False,
    )
    # user_id = Column(Integer, ForeignKey('user.id'))
