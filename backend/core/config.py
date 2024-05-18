import os
from typing import Optional
from pydantic import BaseSettings, EmailStr
from dotenv import load_dotenv
from constants import (
    APP_TITLE, ENV_FILE_NAME,
)
load_dotenv()


class Settings(BaseSettings):
    """Считывать переменные окружения из файла.
    Если значений нет в файле .env, то считываются значения по умолчанию из constants."""
    app_title: str = APP_TITLE
    database_url: str
    secret: str = os.getenv('SECRET')
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        """Файл с переменными окружения."""
        env_file = ENV_FILE_NAME


settings = Settings()
