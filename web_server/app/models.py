"""Models for the database."""
from sqlalchemy import Column, Integer, String

from .database import Base


class Sentences(Base):
    __tablename__ = "sentences"
    id = Column(Integer, primary_key=True, index=True)
    sentence = Column(String)
    labeled = Column(Integer, default=3)
