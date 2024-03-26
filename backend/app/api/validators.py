from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.app.crud import application_crud, application_company_crud
from backend.app.models import Application, ApplicationCompany


async def check_application_exists(
        application_id: int,
        session: AsyncSession,
) -> Application:
    """Проверить существование заявки по id."""
    application = await application_crud.get(application_id, session)
    if application is None:
        raise HTTPException(
            status_code=404,
            detail='Заявка не найдена!'
        )
    return application
