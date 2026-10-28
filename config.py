import os
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Text Summary API"
    environment: str = "development"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"

    openrouter_api_key: str = ""
    openrouter_model: str = "openrouter:nvidia/nemotron-3.5-lightning:free"
    openrouter_max_tokens: int = 2048


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
