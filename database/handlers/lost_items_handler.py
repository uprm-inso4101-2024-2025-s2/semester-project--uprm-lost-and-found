from ..database import Database
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.models import LostItem 
class LostItemsHandler:
    def __init__(self):
        self.database=Database()
        pass

    def createItem(self,i_id:str,i_desc:str,i_pub_date:str,i_photo:str,i_info:str):
        with Session(self.database.engine) as session:
            item=LostItem(id=i_id,description=i_desc,published_date=i_pub_date,photo=i_photo,information=i_info)
            session.add(item)
            session.commit()

        
    def updateItem(self, id:str,i_desc:str=None,i_pub_date:str=None,i_photo:str=None,i_info:str=None):
        with Session(self.database.engine) as session:
            stmt = select(LostItem).where(LostItem.id==id)
            item = session.scalars(stmt).one()

            if i_desc is not None:
                item.description=i_desc
            if i_photo is not None:
                item.photo=i_photo
            if i_pub_date is not None:
                item.published_date=i_pub_date
            if i_info is not None:
                item.information=i_info
            session.commit()
        pass
    def deleteItem(self,id:str):
        with Session(self.database.engine) as session:
            statement=select(LostItem).where(LostItem.id.in_(id))
            item=session.scalars(statement).one()
            session.delete(item)
            session.commit()
        pass
    def getItem(self,id:str):
        with Session(self.database.engine) as session:
            statement=select(LostItem).where(LostItem.id.in_(id))
            item=session.scalars(statement).one()
            if not item:
                print("Database has no such item: "+id)
            return item
        pass
