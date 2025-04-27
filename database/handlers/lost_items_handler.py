from ..database import Database
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.models import LostItem 
from datetime import date
class LostItemsHandler:
    def __init__(self):
        self.database=Database()
        pass

    def createItem(self,i_id:int,i_desc:str, name:str, i_pub_date:str,i_photo:bytes,i_info:str):
        #Changes:

        #i_id: str  -> i_id: int (to follow the Tables and Models Format)
        # i_photo: str -> i_photo : bytes
        with Session(self.database.engine) as session:

            #Create this to pass the date from str to date to match the Tables and models Format
            published_date = date.fromisoformat(i_pub_date)
            item=LostItem(id=i_id,description=i_desc,name = name,published_date=published_date,photo=i_photo,information=i_info)
            session.add(item)
            session.commit()

        
    def updateItem(self, id:int,i_desc:str=None,name : str = None, i_pub_date:str=None,i_photo:bytes=None,i_info:str=None):
        with Session(self.database.engine) as session:
            stmt = select(LostItem).where(LostItem.id==id)
            item = session.scalars(stmt).one()

            if name is not None:
              item.name = name

            if i_desc is not None:
                item.description=i_desc
            if i_photo is not None:
                item.photo=i_photo
            if i_pub_date is not None:
                item.published_date=date.fromisoformat(i_pub_date)
            if i_info is not None:
                item.information=i_info
            session.commit()
        pass
    #Change id str to int
    def deleteItem(self,id:int):
        with Session(self.database.engine) as session:
            statement=select(LostItem).where(LostItem.id ==id)
            item=session.scalars(statement).one()
            session.delete(item)
            session.commit()
        pass
    def getItem(self,id:int):
        with Session(self.database.engine) as session:
            statement=select(LostItem).where(LostItem.id ==id)
            item=session.scalars(statement).one()
            if not item:
                print("Database has no such item: "+ str(id))
            return item
        pass
