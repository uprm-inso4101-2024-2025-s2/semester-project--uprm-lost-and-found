from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
#from database.handlers.users_handler import router as users_router
from database.database import get_db  # ✅ import your DB dependency

app = FastAPI()

# Include the user routes
#app.include_router(users_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Lost & Found UPRM API is running"}

@app.get("/test-db")
def test_connection(db: Session = Depends(get_db)):
    return {"message": "✅ Connected to MySQL on Railway!"}