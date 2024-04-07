from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base import CRUDBase
from schemas.company import CompanyUpdate
from models.company import Company


class CRUDCompany(CRUDBase):
    """CRUD-операции с компаниями."""

    async def check_if_company_exists(
        self,
        company_inn: int,
        session: AsyncSession,
    ):
        """Проверить, существует ли в базе компания с переданным ИНН."""
        db_company = await session.execute(
            select(Company).where(
                Company.company_inn == company_inn
            )
        )
        db_company = db_company.scalars().first()
        return db_company

    async def patch_company_name(
        self,
        db_obj: Company,
        obj_in: str,
        session: AsyncSession,
    ) -> Company:
        """Обновить название компании."""
        db_obj.company_name = obj_in
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


company_crud = CRUDCompany(Company)
