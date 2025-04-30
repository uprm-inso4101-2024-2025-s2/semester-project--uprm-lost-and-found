from fastapi import FastAPI
from database.handlers.users_handler import router as users_router
from database.handlers.lost_items_handler import router as lost_items_router  

app = FastAPI()

# Register routes
app.include_router(users_router, prefix="/api")
app.include_router(lost_items_router, prefix="/api")  # NEW

@app.get("/")
def home():
    return {"message": "Lost & Found UPRM API is running"}
