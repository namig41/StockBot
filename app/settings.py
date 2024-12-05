from functools import lru_cache

import environ
from pydantic_settings import BaseSettings


env = environ.Env()
environ.Env.read_env(".env")


class ProjectSettings(BaseSettings):
    TG_BOT_TOKEN: str = env("TG_BOT_TOKEN")
    GREETING_TEXT: str = env(
        "GREETING_TEXT",
        default=(
            "Добро пожаловать в бот техподдержки.\n"
            "Список доступных команд:\n"
            "/batches - Получить список продуктов\n"
            "/batch - Получить продукт по номеру\n"
            "/add_batch - Добавить новый продукт\n"
        ),
    )
    WEB_API_BASE_URL: str = env("WEB_API_BASE_URL", default="http://localhost:8000")


@lru_cache(1)
def get_settings() -> ProjectSettings:
    return ProjectSettings()
