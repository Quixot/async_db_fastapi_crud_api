from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite+aiosqlite:///./database.db"

    class Config:
        case_sensitive = True


settings = Settings()
