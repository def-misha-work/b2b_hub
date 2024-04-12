from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from copy import deepcopy

from api.validators import check_application_exists
from constants import CLEAR_ROUTE
from core.db import get_async_session
from core.user import get_current_username
from crud import application_crud, application_company_crud
from services.application_process import add_field_to_combined_table
from schemas.application import ApplicationCreate, ApplicationResponse


router = APIRouter()


@router.get(
    '/{application_id}',
    response_model=ApplicationResponse,
    dependencies=[Depends(get_current_username)],
)
async def get_application_by_id(
    application_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> ApplicationResponse:
    """Получить заявку по id."""
    app = await application_crud.get_application_by_id(application_id, session)
    if app:
        extra_data = await application_company_crud.get_objs_by_application_id(application_id, session)
        payer = []
        recipient = []
        for item in extra_data:
            if item.payer_or_recipient_status == 'payer':
                payer.append(item.company_inn)
            elif item.payer_or_recipient_status == 'recipient':
                recipient.append(item.company_inn)
        result_app = ApplicationResponse(
            target_date=app.target_date, cost=app.cost, inn_payer=payer, inn_recipient=recipient,
            tg_user_id=app.tg_user_id, id=app.id
        )
        return result_app


@router.get(
    '/my/{tg_user_id}',
    response_model=list[ApplicationResponse],
    dependencies=[Depends(get_current_username)],
)
async def get_all_applications_by_tg_user(
    tg_user_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> list[ApplicationResponse]:
    """Получить список всех заявок telegram-пользователя."""
    result = []
    applications_ids = await application_crud.get_applications_ids_by_tg_user_id(tg_user_id, session)
    for application_id in applications_ids:
        app = await get_application_by_id(application_id, session)
        result.append(app)
    return result


@router.post(
    CLEAR_ROUTE,
    response_model=ApplicationResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_username)],
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
        new_application.tg_user_id,
        session,
    )
    application_id = new_application_dict.get('id')
    return await get_application_by_id(application_id, session)


@router.delete(
    '/{application_id}',
    response_model=ApplicationResponse,
    status_code=status.HTTP_202_ACCEPTED,
    dependencies=[Depends(get_current_username)],
)
async def remove_application(
        application_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Удалить заявку по id."""
    application = await check_application_exists(application_id, session)
    pairs = await application_company_crud.get_objs_by_application_id(application_id, session)
    for item in pairs:
        await application_company_crud.remove(item, session)

    await application_crud.remove(application, session)
