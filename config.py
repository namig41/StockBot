from functools import lru_cache
import environ

from pydantic_settings import BaseSettings

env = environ.Env()
environ.Env.read_env('.env')

class ProjectSettings(BaseSettings):
    TG_BOT_TOKEN: str = env('TG_BOT_TOKEN')

@lru_cache(1)
def get_settings() -> ProjectSettings:
    return ProjectSettings()