from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_user
from app.schemas.user import User, UserCreate
from app.api.v1.endpoints.health import get_db

router = APIRouter()

@router.get("/", response_model=list[User])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db=db, user=user)

@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.username = user.username
    db_user.email = user.email
    db_user.hashed_password = user.password + "notreallyhashed"  # Simulating password hashing
    db.commit()
    db.refresh(db_user)
    return db_user