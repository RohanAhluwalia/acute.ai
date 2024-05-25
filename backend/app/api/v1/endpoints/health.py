from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/test-db")
async def test_db_connection(db: Session = Depends(get_db)):
    try:
        # Use text to explicitly declare the SQL expression
        result = db.execute(text("SELECT 1"))
        row = result.fetchone()
        # Convert the result to a dictionary
        data = {"result": row[0] if row else None}
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

