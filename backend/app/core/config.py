"""
LIFE OS - Core Configuration (production-ready via env)
"""
from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional
import os


class Settings(BaseSettings):
    APP_NAME: str = "LIFE OS"
    APP_VERSION: str = "0.4.1"
    DEBUG: bool = os.getenv("LIFE_OS_DEBUG", "true").lower() in ("1", "true", "yes")
    API_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = os.getenv("LIFE_OS_ENV", "development")

    SECRET_KEY: str = os.getenv(
        "LIFE_OS_SECRET_KEY",
        "life-os-dev-secret-change-me-in-production-32chars",
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("LIFE_OS_TOKEN_EXPIRE_MINUTES", str(60 * 24 * 7)))

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:////tmp/lifeos.db",
    )

    CORS_ORIGINS: str = os.getenv("LIFE_OS_CORS_ORIGINS", "*")

    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    AI_PROVIDER: str = os.getenv("LIFE_OS_AI_PROVIDER", "auto")

    MEDIA_STORAGE_PATH: str = os.getenv("LIFE_OS_MEDIA_PATH", "/tmp/lifeos_media")
    MAX_UPLOAD_MB: int = int(os.getenv("LIFE_OS_MAX_UPLOAD_MB", "25"))

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"

    @property
    def cors_origins_list(self) -> list[str]:
        if self.CORS_ORIGINS.strip() == "*":
            return ["*"]
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "production"

    @property
    def llm_enabled(self) -> bool:
        if self.AI_PROVIDER == "rules":
            return False
        if self.AI_PROVIDER == "openai":
            return bool(self.OPENAI_API_KEY)
        return bool(self.OPENAI_API_KEY)


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
