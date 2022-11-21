from pydantic import BaseSettings
from typing import List
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "sqlite+aiosqlite:///./database.db"
    PROJECT_NAME: str = "Async FastAPI API"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:4200",
                                              "http://localhost:3000", "http://localhost:8080"]

    class Config:
        case_sensitive = True


settings = Settings()
