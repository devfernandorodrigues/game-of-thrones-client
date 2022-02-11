from typing import List, Optional

from pydantic import BaseModel


class Member(BaseModel):
    name: str
    slug: str


class House(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    members: Optional[List[Member]] = []


class Character(BaseModel):
    name: str
    slug: str
    house: Optional[House] = None
    quotes: Optional[List[str]] = []


class Quote(BaseModel):
    sentence: str
    character: Character
