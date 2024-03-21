from fastapi import APIRouter

from backend.constants import (
    APPLICATION_ROUTER_PREFIX, APPLICATION_ROUTER_TAG,
)
from backend.app.api.endpoints import (
    application_router,
)

main_router = APIRouter()

main_router.include_router(
    application_router,
    prefix=APPLICATION_ROUTER_PREFIX,
    tags=[APPLICATION_ROUTER_TAG],
)
