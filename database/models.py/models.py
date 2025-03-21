from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database.database import Base

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