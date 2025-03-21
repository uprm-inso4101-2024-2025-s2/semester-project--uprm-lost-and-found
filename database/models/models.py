from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase

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
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="user")  # 'admin' or 'user'

class Matches(Base):
    __tablename__ = "matches"

    m_id = Column(Integer, primary_key=True, index=True)
    l_id = Column(Integer, ForeignKey('lostitems.l_id'), nullable=False)
    f_id = Column(Integer, ForeignKey('founditems.f_id'), nullable=False)
    match_confidence_score = Column(Float, nullable=False)
    date_matched = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)

import datetime;

class LostItem(Base):
    __tablename__="LostItems"
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(120))

    # change string to a date Object
    published_date:Mapped[str]= mapped_column(String())
    photo: Mapped[str] = mapped_column(String())
    information: Mapped[str] = mapped_column(String(500))
    