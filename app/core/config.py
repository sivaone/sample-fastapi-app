from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Local Library API"
    DATABASE_URL: str = "sqlite:///./library.db"
    LOG_LEVEL: str = "INFO"

    class Config:
        case_sensitive = True


settings = Settings()
