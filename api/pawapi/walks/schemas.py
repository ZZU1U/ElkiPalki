from datetime import datetime
from typing import Any
from pydantic import BaseModel


class WalkBase(BaseModel):
    date: datetime
    duration: int
    animal_id: int
    user_id: int


class WalkRead(WalkBase):
    id: int


class WalkCreate(WalkBase):
    pass


class WalkUpdate(WalkBase):
    pass
