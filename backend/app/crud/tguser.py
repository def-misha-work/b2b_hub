from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.crud.base import CRUDBase
from backend.app.models.tguser import TgUser


class CRUDTgUser(CRUDBase):
    """CRUD-операции с telegram-пользователями."""

    async def check_if_tguser_exists(self, tg_user_id: int, session: AsyncSession):
        """Добавить в таблицу telegram-пользователей новую запись, если такого пользователя еще нет."""
        db_tguser = await session.execute(
            select(TgUser).where(
                TgUser.tg_user_id == tg_user_id
            )
        )
        db_tguser = db_tguser.scalars().first()
        return db_tguser is not None


tguser_crud = CRUDTgUser(TgUser)
