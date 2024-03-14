from pydantic import BaseSettings

from backend.constants import (
    APP_TITLE, ENV_FILE_NAME,
)


class Settings(BaseSettings):
    """Считывать переменные окружения из файла.
    Если значений нет в файле .env, то считываются значения по умолчанию из constants."""
    app_title: str = APP_TITLE
    database_url: str

    class Config:
        """Файл с переменными окружения."""
        env_file = ENV_FILE_NAME


settings = Settings()
