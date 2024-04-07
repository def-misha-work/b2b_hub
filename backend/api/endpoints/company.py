from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from core.user import current_user
from crud import company_crud
from schemas.company import CompanyUpdate


router = APIRouter()


@router.patch(
    '/{company_id}/update',
    response_model=CompanyUpdate,
    dependencies=[Depends(current_user)],
)
async def check_or_update_company_name(
    company_inn: int,
    company_name: str,
    session: AsyncSession = Depends(get_async_session),
) -> CompanyUpdate:
    """Обновить название компании, если его нет."""
    company = await company_crud.check_if_company_exists(
        company_inn=company_inn, session=session)
    if not company.company_name:
        company = await company_crud.patch_company_name(
            db_obj=company,
            obj_in=company_name,
            session=session,
        )
        return CompanyUpdate(
            company_name=company.company_name,
            company_inn=company.company_inn,
            tg_user_id=company.tg_user_id,
        )
