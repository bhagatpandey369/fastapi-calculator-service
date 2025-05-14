from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = 8000
    ENV: str = "development"


settings = Settings()
