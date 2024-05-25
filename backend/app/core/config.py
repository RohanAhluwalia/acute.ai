from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    METRIPORT_API_KEY: str
    METRIPORT_BASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

