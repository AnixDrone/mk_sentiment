from typing import List, Optional
from pydantic import BaseModel


class SentenceBase(BaseModel):
    sentence: str
    labeled: Optional[int] = 3


class Sentence(SentenceBase):
    id: int
    class Config:
        orm_mode = True
