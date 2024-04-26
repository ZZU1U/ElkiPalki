from datetime import datetime
from pydantic import BaseModel
from typing import Any
from .enums import AnimalStatus


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
    walks: Any  # TODO should probably change this
