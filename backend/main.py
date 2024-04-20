from fastapi import FastAPI

from api.routers import main_router
from core.config import settings

app = FastAPI(title=settings.app_title)

app.include_router(main_router)
