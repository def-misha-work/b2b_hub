from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from core.user import get_current_username
from crud import company_crud
from schemas.company import CompanyBase, CompanyUpdate


router = APIRouter()


@router.patch(
    '/{company_id}/update',
    response_model=CompanyUpdate,
    dependencies=[Depends(get_current_username)],
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


@router.get(
    '/my/{tg_user_id}',
    response_model=list[CompanyBase],
    dependencies=[Depends(get_current_username)],
)
async def get_all_companies_by_tg_user(
    tg_user_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> list[CompanyBase]:
    """Получить список всех компаний telegram-пользователя."""
    result = []
    companies = await company_crud.get_companies_by_tg_user_id(tg_user_id, session)
    for company in companies:
        company = CompanyBase(company_name=company.company_name,
                              company_inn=company.company_inn)
        result.append(company)
    return result
