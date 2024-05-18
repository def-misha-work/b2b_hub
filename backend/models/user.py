from sqlalchemy import Column, BigInteger, Boolean, String

from core.db import Base


class User(Base):
    """Модель пользователя."""
    id: int = Column(BigInteger, unique=True,  primary_key=True)
    username = Column(String, unique=True, nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    password = Column(String, nullable=False)
