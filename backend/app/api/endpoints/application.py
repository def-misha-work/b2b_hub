from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from copy import deepcopy

from backend.app.core.db import get_async_session
from backend.app.crud import application_crud
from backend.app.services.application_process import add_field_to_combined_table
from backend.app.schemas.application import ApplicationCreate, ApplicationResponse
from backend.constants import CLEAR_ROUTE

router = APIRouter()


@router.post(
    CLEAR_ROUTE,
    response_model=ApplicationResponse,
    # dependencies=[Depends(current_user)],
    response_model_exclude_none=True,
)
async def create_new_application(
    application_data: ApplicationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Создать новую заявку."""
    new_application = await application_crud.create_application(application_data, session)
    new_application_dict = deepcopy(new_application.__dict__)
    await add_field_to_combined_table(
        application_data.inn_payer,
        application_data.inn_recipient,
        new_application.id,
        session,
    )
    return ApplicationResponse(
        target_date=application_data.target_date, cost=application_data.cost,
        inn_payer=application_data.inn_payer, inn_recipient=application_data.inn_recipient,
        id=new_application_dict.get('id'))
