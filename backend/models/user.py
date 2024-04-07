from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass
