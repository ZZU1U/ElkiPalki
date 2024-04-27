from datetime import datetime
from pydantic import BaseModel
from typing import Any
from pawapi.enums import AnimalStatus


class AnimalBase(BaseModel):
    name: str
    species: str
    age: int
    description: str
    image: str | None
    status: AnimalStatus | None
    last_donation: datetime | None
    food_donated: int | None
    food_daily: int | None


class AnimalChange(AnimalBase):
    id: int


class AnimalRead(AnimalBase):
    id: int


class AnimalWrite(AnimalBase):
    pass
