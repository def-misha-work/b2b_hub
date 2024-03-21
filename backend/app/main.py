from fastapi import FastAPI

from backend.app.api.routers import main_router
from backend.app.core.config import settings

app = FastAPI(title=settings.app_title)

app.include_router(main_router)
