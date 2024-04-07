from fastapi import APIRouter

from constants import (
    APPLICATION_ROUTER_PREFIX, APPLICATION_ROUTER_TAG,
    COMPANY_ROUTER_PREFIX, COMPANY_ROUTER_TAG,
    TGUSER_ROUTER_PREFIX, TGUSER_ROUTER_TAG,
)
from api.endpoints import (
    application_router, company_router, tguser_router, user_router,
)

main_router = APIRouter()

main_router.include_router(
    application_router,
    prefix=APPLICATION_ROUTER_PREFIX,
    tags=[APPLICATION_ROUTER_TAG],
)

main_router.include_router(
    company_router,
    prefix=COMPANY_ROUTER_PREFIX,
    tags=[COMPANY_ROUTER_TAG],
)

main_router.include_router(
    tguser_router,
    prefix=TGUSER_ROUTER_PREFIX,
    tags=[TGUSER_ROUTER_TAG],
)

main_router.include_router(user_router)
