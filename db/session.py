from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
