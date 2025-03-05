from sqlalchemy.orm import Session
from database.models import User
from passlib.context import CryptContext

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Hashes the password using bcrypt."""
    return pwd_context.hash(password)

def create_user(db: Session, name: str, email: str, password: str, role="user"):
    """Creates a new user with hashed password."""
    password_hash = hash_password(password)  # Hash password before storing
    user = User(name=name, email=email, password_hash=password_hash, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    """Retrieves a user by email."""
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    """Retrieves a user by ID."""
    return db.query(User).filter(User.id == user_id).first()