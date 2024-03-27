from typing import List
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.crud.base import CRUDBase
from backend.app.models import ApplicationCompany


class CRUDApplicationCompany(CRUDBase):
    """CRUD-операции с заявками."""
    ...

    async def get_objs_by_application_id(
            self,
            application_id: int,
            session: AsyncSession,
    ) -> List[int]:
        query = await session.execute(
            select(ApplicationCompany).where(
                ApplicationCompany.id_application == application_id))
        return query.scalars().all()


application_company_crud = CRUDApplicationCompany(ApplicationCompany)
