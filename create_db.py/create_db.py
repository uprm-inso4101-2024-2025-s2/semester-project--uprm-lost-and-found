from database.database import engine
from database.models import Base

# Create tables in the database
Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")