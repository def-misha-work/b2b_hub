from fastapi import APIRouter, HTTPException, Depends

from core.user import get_current_username
from schemas.user import UserBase

router = APIRouter()


# @router.get("/me")
# def read_current_user(
#         user_data: UserBase = Depends(get_current_username)
# ):
#     return {"username": user_data.username}


@router.delete(
    '/{id}',
    tags=['users'],
    deprecated=True,
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        status_code=405,
        detail="Удаление пользователей запрещено!"
    )
