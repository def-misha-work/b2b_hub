from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core.db import get_async_session
from backend.app.crud import tguser_crud
from backend.app.schemas.tguser import TgUserCreate, TgUserDB
from backend.constants import CLEAR_ROUTE

router = APIRouter()


@router.post(
    CLEAR_ROUTE,
    response_model=TgUserDB,
    response_model_exclude_none=True,
)
async def create_new_tguser(
    tguser_data: TgUserCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Создать нового telegram-пользователя."""
    if not await tguser_crud.check_if_tguser_exists(tguser_data.tg_id, session):
        new_user = await tguser_crud.create(tguser_data, session)
        return new_user
    else:
        return tguser_data
