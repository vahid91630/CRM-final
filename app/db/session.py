from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import settings

# ساختن engine برای اتصال async
engine = create_async_engine(settings.database_url, echo=True)

# ساختن session
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
