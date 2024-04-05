from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from backend.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass
