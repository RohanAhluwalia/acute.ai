from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env.

class Settings(BaseSettings):
    database_url: str = "postgresql://defaultusername:defaultpassword@db/diabetes_db"

    class Config:
        env_file = ".env"

settings = Settings()


# Create the SQLAlchemy engine
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
