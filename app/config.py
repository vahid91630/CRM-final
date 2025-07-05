from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    webhook_url: str
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
