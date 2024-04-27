from datetime import datetime
from pydantic import BaseModel
from typing import Any
from pawapi.enums import Role


class UserBase(BaseModel):
    name: str
    role: Role


class UserRead(UserBase):
    id: int


class UserWrite(UserBase):
    pass
