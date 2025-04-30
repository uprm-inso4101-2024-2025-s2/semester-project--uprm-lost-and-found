from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import uuid4
from datetime import datetime

from ..database import get_db, Database
from ..models.models import LostItem

router = APIRouter()

# ────────────────────────────────────────
# CLASS: LostItemsHandler
# ────────────────────────────────────────
class LostItemsHandler:
    def __init__(self):
        self.database = Database()

    def createItem(self, i_id: str, i_desc: str, i_pub_date: str, i_photo: str, i_info: str):
        with Session(self.database.engine) as session:
            item = LostItem(
                id=i_id,
                description=i_desc,
                published_date=i_pub_date,
                photo=i_photo,
                information=i_info
            )
            session.add(item)
            session.commit()

    def updateItem(self, id: str, i_desc: str = None, i_pub_date: str = None, i_photo: str = None, i_info: str = None):
        with Session(self.database.engine) as session:
            stmt = select(LostItem).where(LostItem.id == id)
            item = session.scalars(stmt).one()

            if i_desc is not None:
                item.description = i_desc
            if i_photo is not None:
                item.photo = i_photo
            if i_pub_date is not None:
                item.published_date = i_pub_date
            if i_info is not None:
                item.information = i_info
            session.commit()

    def deleteItem(self, id: str):
        with Session(self.database.engine) as session:
            stmt = select(LostItem).where(LostItem.id.in_([id]))
            item = session.scalars(stmt).one()
            session.delete(item)
            session.commit()

    def getItem(self, id: str):
        with Session(self.database.engine) as session:
            stmt = select(LostItem).where(LostItem.id.in_([id]))
            item = session.scalars(stmt).one()
            if not item:
                print("Database has no such item: " + id)
            return item

# ────────────────────────────────────────
# API Endpoint: Submit Lost Item
# ────────────────────────────────────────
@router.post("/lost-items/")
def submit_lost_item(data: dict, db: Session = Depends(get_db)):
    try:
        item = LostItem(
            id=str(uuid4()),
            l_description=data.get("description"),
            l_publishdate=datetime.utcnow().date(),
            l_photo=",".join(data.get("images", [])),
            l_information=(
                f"{data.get('foundLocation')} | "
                f"{data.get('contactName')} | "
                f"{data.get('contactEmail')} | "
                f"{data.get('contactPhone')} | "
                f"{data.get('comments')}"
            )
        )
        db.add(item)
        db.commit()
        return {"message": "Lost item submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
