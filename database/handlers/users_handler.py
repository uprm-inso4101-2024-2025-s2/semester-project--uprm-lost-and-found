from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.dao.users_dao import create_user, get_user_by_email, get_user_by_id
from database.database import get_db

router = APIRouter()

@router.post("/users/")
def register_user(name: str, email: str, password: str, db: Session = Depends(get_db)):
    """Registers a new user."""
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = create_user(db, name, email, password)
    return {"message": "User created successfully", "user_id": user.id}

@router.get("/users/{user_id}")
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieves a user by ID."""
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email, "role": user.role}