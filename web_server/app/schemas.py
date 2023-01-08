"""Schema for the database models."""
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from typing import Optional
from pydantic import BaseModel


class SentenceBase(BaseModel):
    sentence: str
    labeled: Optional[int] = 3


class Sentence(SentenceBase):
    id: int

    class Config:
        orm_mode = True
