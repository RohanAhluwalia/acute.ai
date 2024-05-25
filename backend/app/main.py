from fastapi import FastAPI
from app.api.v1.endpoints import data, users, health, metriport
from app.db.base import Base  # Ensure this is the correct Base import
from app.db.session import engine
from app.models import user

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}

app.include_router(data.router, prefix="/data")
app.include_router(users.router, prefix="/users")
app.include_router(health.router, prefix="/health")
app.include_router(metriport.router, prefix="/metriport")

# Ensure all tables are created
user.Base.metadata.create_all(bind=engine)
