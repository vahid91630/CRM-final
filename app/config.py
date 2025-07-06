from pydantic import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    WEBHOOK_URL: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
