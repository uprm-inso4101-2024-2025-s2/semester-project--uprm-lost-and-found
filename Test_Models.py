
#This file is created with the purpose of testing  each of the models in the the models.py file.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models.models import Base, User, LostItem, Location, ClaimItems, FoundItems, Matches, Comments
from datetime import date
#Run by installing pytest
from datetime import date
import pytest
import os

# to test the files locally test.db
DATA_URL = "sqlite:///./test.db"
engine = create_engine(DATA_URL, echo = True)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

#To create the Pytest functions(2) I search for internet help
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    if os.path.exists("./test.db"):
        os.remove("./test.db")
    Base.metadata.create_all(bind=engine)
    yield  # Allow tests to run
    if os.path.exists("./test.db"):
        os.remove("./test.db")


@pytest.fixture
def test_models():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_user(test_models):
    db = test_models

    new_user = User(name = "Paty", email = "test@upr.edu", password_hash = "NotaPassword", profile_photo =b"imagebytes", role = "user" )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    assert new_user.name == "Paty"
    assert new_user.email == "test@upr.edu"
    assert new_user.password_hash == "NotaPassword"
    assert new_user.profile_photo == b"imagebytes"
    assert new_user.role == "user"
    assert new_user.id is not None

def  test_LostItem(test_models):
    
    db = test_models

    new_user = User(name = "Paty", email = "tesit@upr.edu", password_hash = "NotaPassword", profile_photo =b"imagebytes", role = "user" )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    lost = LostItem(name="Blue iphone", description= "Lost Phone", published_date= date(2025, 4, 24), photo = b"photo", information = "Iphone 5 Lost in S 113", u_id =new_user.id)
    db.add(lost)
    db.commit()
    db.refresh(lost)

    assert lost.name == "Blue iphone"
    assert lost.description == "Lost Phone"
    assert lost.published_date == date(2025, 4, 24)
    assert lost.photo == b"photo"
    assert lost.information == "Iphone 5 Lost in S 113"
    assert lost.u_id == new_user.id

def test_FoundItems(test_models):
    db = test_models

    new_user = User(name = "Paty", email = "tesiit@upr.edu", password_hash = "NotaPassword", profile_photo =b"imagebytes", role = "user" )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    location = Location(name = "S 113", coordinates= "18.2345, -59.8992")
    db.add(location)
    db.commit()
    db.refresh(location)

    
    found = FoundItems(photo ="test_image.jpg", description = "Found $20", published_date=date(2025, 4, 24), place_found="S- 113", additional_details= "It was on the last row of seats",u_id=new_user.id, p_id=location.id) 
    db.add(found)
    db.commit()
    db.refresh(found)

    assert found.photo == "test_image.jpg" 
    assert found.description == "Found $20"
    assert found.published_date == date(2025, 4, 24)
    assert found.place_found == "S- 113"
    assert found.additional_details =="It was on the last row of seats"
    assert found.u_id == new_user.id
    assert found.p_id == location.id

def test_location(test_models):
    db = test_models

    

    location = Location(name = "S 113", coordinates= "18.2345, -59.8992")
    db.add(location)
    db.commit()
    db.refresh(location)

    assert location.name == "S 113"
    assert location.coordinates ==  "18.2345, -59.8992"


def test_ClaimItems(test_models):
     db = test_models

     new_user = User(name = "Paty", email = "testy@upr.edu", password_hash = "NotaPassword", profile_photo =b"imagebytes", role = "user" )
     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     location = Location(name = "S 113", coordinates= "18.2345, -59.8992")
     db.add(location)
     db.commit()
     db.refresh(location)

     

     
     found = FoundItems(photo = "test_image.jpg", description = "Found $20", published_date=date(2025, 4, 24), place_found="S- 113", additional_details= "It was on the last row of seats",u_id=new_user.id, p_id=location.id) 

     #found = FoundItems(photo = b"photo", description = "Found $20", published_date=date(2025, 4, 24), place_found="S- 113", additional_details= "It was on the last row of seats",u_id=new_user.id, p_id=location.id) 
     db.add(found)
     db.commit()
     db.refresh(found)

     claim = ClaimItems(f_id = found.id, u_id = new_user.id, status= "pending")
     db.add(claim)
     db.commit()
     db.refresh(claim)

     assert claim.status == "pending"
     assert claim.f_id == found.id
     assert claim.u_id == new_user.id

def test_Comments(test_models):
     db = test_models

     new_user = User(name = "Paty", email = "trest@upr.edu", password_hash = "NotaPassword", profile_photo =b"imagebytes", role = "user" )
     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     lost = LostItem(name="Blue iphone",description= "Lost Phone", published_date= date(2025, 4, 24), photo = b"photo", information = "Iphone 5 Lost in S 113", u_id =new_user.id)
     db.add(lost)
     db.commit()
     db.refresh(lost)

     comment = Comments(content= "I found a Iphone 5", publish_date=date(2025, 4, 24), u_id = new_user.id, l_id = lost.id)
     db.add(comment)
     db.commit()
     db.refresh(comment)

     assert comment.content ==  "I found a Iphone 5"
     assert comment.publish_date == date(2025, 4, 24)
     assert comment.u_id == new_user.id
     assert comment.l_id == lost.id

def test_matches(test_models):
     db = test_models

     new_user = User(name = "Paty", email = "ttest@upr.edu", password_hash = "NotaPassword", profile_photo =b"imagebytes", role = "user" )
     db.add(new_user)
     db.commit()
     db.refresh(new_user)

     lost = LostItem(name="Blue iphone",description= "Lost Phone", published_date= date(2025, 4, 24), photo = b"photo", information = "Iphone 5 Lost in S 113", u_id =new_user.id)
     db.add(lost)
     db.commit()
     db.refresh(lost)

     location = Location(name = "S 113", coordinates= "18.2345, -59.8992")
     db.add(location)
     db.commit()
     db.refresh(location)

     
     

    
     found = FoundItems(photo = "test_image.jpg", description = "Found $20", published_date=date(2025, 4, 24), place_found="S- 113", additional_details= "It was on the last row of seats",u_id=new_user.id, p_id=location.id) 
     db.add(found)
     db.commit()
     db.refresh(found)

     import datetime

     matches = Matches(l_id = lost.id, f_id = found.id, match_confidence_score= 0.80, status = "pending", date_matched=datetime.datetime(2025, 4, 24))
     db.add(matches)
     db.commit()
     db.refresh(matches)

     assert matches.l_id == lost.id
     assert matches.f_id == found.id
     assert matches.match_confidence_score == 0.80
     assert matches.status == "pending"
     assert matches.date_matched == datetime.datetime(2025, 4, 24)
     #print("Lost item id: ", lost.id, " Found item id: ",  found.id, "Score: ", matches.match_confidence_score, "Status: ", matches.status, " Date: ", matches.date_matched)

