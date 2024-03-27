from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.crud.base import CRUDBase
from backend.app.models.company import Company


class CRUDCompany(CRUDBase):
    """CRUD-операции с компаниями."""

    async def check_if_company_exists(
            self,
            company_inn: int,
            session: AsyncSession,
    ):
        """Добавить в таблицу компаний новую запись, если такой компании еще нет."""
        db_company = await session.execute(
            select(Company).where(
                Company.company_inn == company_inn
            )
        )
        db_company = db_company.scalars().first()
        return db_company is not None


company_crud = CRUDCompany(Company)
