from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
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

class LostItem(Base):
    __tablename__ = "lostitems"  # ✅ lowercase + matches ForeignKey

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(120))
    published_date: Mapped[str] = mapped_column(String(50))
    photo: Mapped[str] = mapped_column(String(255))
    information: Mapped[str] = mapped_column(String(500))

class FoundItem(Base):
    __tablename__ = "founditems"  # ✅ lowercase + matches ForeignKey

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(120))
    found_date: Mapped[str] = mapped_column(String(50))
    photo: Mapped[str] = mapped_column(String(255))
    location: Mapped[str] = mapped_column(String(100))

class Matches(Base):
    __tablename__ = "matches"

    m_id = Column(Integer, primary_key=True, index=True)
    l_id = Column(Integer, ForeignKey('lostitems.id'), nullable=False)   # ✅ correct
    f_id = Column(Integer, ForeignKey('founditems.id'), nullable=False)  # ✅ correct
    match_confidence_score = Column(Float, nullable=False)
    date_matched = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)
