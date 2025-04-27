from sqlalchemy import Column, Integer, String, Float, Date,DateTime, ForeignKey,LargeBinary,Enum,DATE
from sqlalchemy.orm import DeclarativeBase
from datetime import date



from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Users" 

    id = Column("U_ID",Integer, primary_key=True, index=True)
    name = Column("U_Username",String(100), nullable=False)
    email = Column("U_Email",String(100), unique=True, nullable=False)
    password_hash = Column("U_Password",String(500), nullable=False)
    #adding missing column according  to Tables : Profile photo
    profile_photo = Column("U_ProfilePhoto",LargeBinary, nullable= False)
    role = Column(String(20), default="user")  # 'admin' or 'user'

class Matches(Base):
    __tablename__ = "Matches"

    m_id = Column("M_ID",Integer, primary_key=True, index=True)
    l_id = Column(Integer, ForeignKey('LostItems.L_ID'), nullable=False)
    f_id = Column(Integer, ForeignKey('FoundItems.F_ID'), nullable=False)
    match_confidence_score = Column("M_MatchScore",Float, nullable=False)
    date_matched = Column("M_DateMatched",DateTime, nullable=False)
    status = Column("M_Status",String(20), nullable=False)

import datetime

class LostItem(Base):
    __tablename__="LostItems"
    id: Mapped[int] = mapped_column("L_ID",primary_key=True)
    description: Mapped[str] = mapped_column("L_Description",String(120), nullable = False)
    #Adding Lost item name to match Frontend
    name : Mapped[str] = mapped_column("L_name", String(120), nullable = False)
    # change string to a date Object
    published_date:Mapped[date]= mapped_column("L_PublishDate",Date, nullable = False)
    photo: Mapped[bytes] = mapped_column("L_Photo",LargeBinary)
    information: Mapped[str] = mapped_column("L_Information",String(500))
    #adding missing u_id from the LostItems Table.txt
    u_id =  mapped_column(ForeignKey("Users.U_ID"))

class FoundItems(Base):
    __tablename__ = "FoundItems"
    id = Column("F_ID", Integer,primary_key = True, autoincrement = True  )
    photo= Column("F_Photo", String(500), nullable= True )
    description = Column("F_Description",String(120), nullable = False )
    published_date = Column("F_PublishDate", Date, nullable= False)
    place_found = Column("F_PlaceFound",String(20), nullable= True)
    additional_details = Column("F_AdditionalDetails", String(500), nullable=True )
    u_id = Column(Integer, ForeignKey("Users.U_ID", ondelete="CASCADE") , nullable=False)
    p_id = Column(Integer, ForeignKey("Location.P_ID", ondelete= "CASCADE"),nullable = False)

class ClaimItems(Base):
    __tablename__= "ClaimItems"
    id = Column("CR_ID", Integer,primary_key= True, autoincrement=True )
    f_id = Column(Integer, ForeignKey("FoundItems.F_ID",ondelete="CASCADE"), nullable= False)
    u_id = Column(Integer, ForeignKey("Users.U_ID", ondelete="CASCADE"), nullable = False)
    status = Column(Enum('pending', 'claimed', 'declined'), default='pending')


class Location(Base):
    __tablename__ = "Location"
    id = Column("P_ID", Integer, primary_key= True, autoincrement= True)
    name = Column("P_Name", String(20), nullable= False)
    coordinates = Column("P_Coordinates", String(30), nullable= False)

class Comments(Base):
    __tablename__ = "Comments"
    id = Column("C_ID", Integer, primary_key= True, autoincrement=True)
    content = Column("C_Content", String(500), nullable= False)
    publish_date = Column("C_PublishDate",Date , nullable= False)
    u_id= Column(Integer, ForeignKey("Users.U_ID", ondelete="CASCADE"), nullable = False)
    l_id= Column(Integer, ForeignKey("LostItems.L_ID", ondelete="CASCADE"), nullable = False)





    