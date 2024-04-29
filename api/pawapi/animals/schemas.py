from datetime import datetime
from pydantic import BaseModel

from ..db.enums import AnimalStatus


class AnimalBase(BaseModel):
    name: str
    species: str
    age: int
    description: str
    image: str | None = None
    status: AnimalStatus | None = None
    last_donation: datetime | None = None
    food_donated: int | None = None
    food_daily: int | None = None


class AnimalUpdate(AnimalBase):
    id: int


class AnimalRead(AnimalBase):
    id: int


class AnimalCreate(AnimalBase):
    pass
