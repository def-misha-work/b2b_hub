from fastapi import APIRouter

from constants import (
    APPLICATION_ROUTER_PREFIX, APPLICATION_ROUTER_TAG,
    TGUSER_ROUTER_PREFIX, TGUSER_ROUTER_TAG,
)
from api.endpoints import (
    application_router, tguser_router,
)

main_router = APIRouter()

main_router.include_router(
    application_router,
    prefix=APPLICATION_ROUTER_PREFIX,
    tags=[APPLICATION_ROUTER_TAG],
)

main_router.include_router(
    tguser_router,
    prefix=TGUSER_ROUTER_PREFIX,
    tags=[TGUSER_ROUTER_TAG],
)
