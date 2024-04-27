from datetime import datetime
from pydantic import BaseModel
from typing import Any
from pawapi.enums import Role


class UserBase(BaseModel):
    name: str
    role: Role
    walks: Any


class UserRead(UserBase):
    id: int


class UserWrite(UserBase):
    pass
