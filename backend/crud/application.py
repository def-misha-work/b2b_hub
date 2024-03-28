from typing import Optional, List
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from models import Application


class CRUDApplication(CRUDBase):
    """CRUD-операции с заявками."""
    ...

    async def create_application(
            self,
            application,
            session: AsyncSession,
    ):
        """Создать новую заявку."""
        application_data = application.dict()
        new_application = Application(
            target_date=application_data['target_date'],
            cost=application_data['cost'],
            tg_user_id=application_data['tg_user_id'],
        )
        session.add(new_application)
        await session.commit()
        await session.refresh(new_application)
        return new_application

    async def get_application_by_id(
            self,
            application_id: int,
            session: AsyncSession,
    ) -> Optional[Application]:
        """Получить заявку по id."""
        db_application = await session.execute(
            select(Application).where(
                Application.id == application_id
            )
        )
        return db_application.scalars().first()

    async def get_applications_ids_by_tg_user_id(
            self,
            tg_user_id: int,
            session: AsyncSession,
    ) -> Optional[List[Application]]:
        """Получить все id заявок по id telegram-пользователя."""
        db_applications = await session.execute(
            select(Application.id).where(
                Application.tg_user_id == tg_user_id
            )
        )
        return db_applications.scalars().all()


application_crud = CRUDApplication(Application)
