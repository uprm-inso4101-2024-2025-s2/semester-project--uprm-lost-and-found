#Creating Found Items handler
from ..database import Database
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.models import FoundItems
from datetime import date
from ..models.models import FoundItems, User, Location

class FoundItemshandler:
    def __init__(self):
        self.database=Database()
        pass
    # createItem function creates a new found item entry in the database 
    def createItem(self, description:str, published_date: str, place_found : str, additional_details:str, photo: str, contact_name: str, cotact_email:str):
        with Session(self.database.engine) as session:

            published_date = date.fromisoformat(published_date)
            #Creating users from
            user = session.query(User).filter(User.email == cotact_email).first()
            if not user:
                user = User(name = contact_name, email = cotact_email, password_hash= "placeholder" , profile_photo =b"" , role ="user")
                session.add(user)
                session.commit()
                session.refresh(user)

        location = session.query(Location).filter(Location.name == place_found).first()
        if not location:
            #To match the frontend form for the moment the coordinates are dummy
            location = Location(name = place_found,coordinates = "0.0")
            session.add(location)
            session.commit()
            session.refresh(location)

        found  = FoundItems(photo = photo,description = description, published_date = published_date, place_found=place_found, additional_details= additional_details, u_id = user.id, p_id = location.id )
        session.add(found)
        session.commit()

    def getItem(self, id:int):
        with Session(self.database.engine) as session:
            statement = select(FoundItems).where(FoundItems.id == id)
            item = session.scalars(statement).one_or_none()
            if not item:
                print("No such found item with ID:", id)
            return item
    def deleteItem(self, id:int):
        with Session(self.database.engine) as session:
            statement = select(FoundItems).where(FoundItems.id ==id)
            item = session.scalars(statement).one_or_none()
            if item:
                session.delete(item)
                session.commit()

    def updateItem(self, id:int, description : str = None, published_date : str = None, photo : str = None, place_found : str = None, additional_details : str = None):
        with Session(self.database.engine) as session:
            statement = select(FoundItems).where(FoundItems.id == id)
            item = session.scalars(statement).one_or_none()
            if not item:
                print(" No such found item: ", id)
                return
            if description:
                item.description = description
            if published_date:
                item.published_date = date.fromisoformat(published_date)

            if photo:
                item.photo = photo

            if place_found:
                item.place_found = place_found

            if additional_details:
                item.additional_details = additional_details

            session.commit()


