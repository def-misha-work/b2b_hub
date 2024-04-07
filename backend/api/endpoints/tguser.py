from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from core.user import current_user
from crud import tguser_crud
from schemas.tguser import TgUserCreate, TgUserDB
from constants import CLEAR_ROUTE

router = APIRouter()


@router.post(
    CLEAR_ROUTE,
    response_model=TgUserDB,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(current_user)],
)
async def create_new_tguser(
    tguser_data: TgUserCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Проверить наличие и создать нового telegram-пользователя."""
    if not await tguser_crud.check_if_tguser_exists(tguser_data.tg_user_id, session):
        new_user = await tguser_crud.create(tguser_data, session)
        return new_user
    else:
        return JSONResponse(
            content={"message": f"User {tguser_data.tg_user_id} already exists"},
            status_code=status.HTTP_200_OK
        )
