from fastapi import FastAPI
from database.handlers.users_handler import router as users_router

app = FastAPI()

# Include the user routes
app.include_router(users_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Lost & Found UPRM API is running"}