from fastapi import FastAPI
from .config import settings
from .models import Base, engine
from .routers import patients, data

app = FastAPI()

# Create the database tables in the correct order
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(data.router, prefix="/data", tags=["data"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Management App"}
