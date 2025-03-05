from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Temporary SQLite database (change this to PostgreSQL/MySQL later)
DATABASE_URL = "sqlite:///./test.db"

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    """Creates a new database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()