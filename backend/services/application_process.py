from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from crud import company_crud
from models import ApplicationCompany, Company


async def create_or_check_company(company_inn: int, tg_user_id: int, session: AsyncSession):
    """Проверяет, существует ли компания с таким ИНН, и, если нет, создает новую."""
    company_exists = await company_crud.check_if_company_exists(company_inn=company_inn, session=session)
    if not company_exists:
        new_company_record = Company(company_inn=company_inn, tg_user_id=tg_user_id)
        session.add(new_company_record)
        await session.commit()


async def add_field_to_combined_table(
    inn_payer: List[int],
    inn_recipient: List[int],
    application_id: int,
    tg_user_id: int,
    session: AsyncSession,
):
    """Добавить запись в таблицу ApplicationCompany для связи id заявки и ИНН компании, а также в таблицу Company."""
    for inn in inn_payer:
        await create_or_check_company(company_inn=inn, tg_user_id=tg_user_id, session=session)
        new_record = ApplicationCompany(
            id_application=application_id,
            company_inn=inn,
            payer_or_recipient_status="payer"
        )
        session.add(new_record)

    for inn in inn_recipient:
        await create_or_check_company(company_inn=inn, tg_user_id=tg_user_id, session=session)
        new_record = ApplicationCompany(
            id_application=application_id,
            company_inn=inn,
            payer_or_recipient_status="recipient"
        )
        session.add(new_record)

    await session.commit()
