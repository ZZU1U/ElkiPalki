from pydantic import BaseModel
from pawapi.enums import Role


class UserBase(BaseModel):
    phone: str | None = None
    name: str


class UserRead(UserBase):
    id: int
    role: Role


class UserWrite(UserBase):
    role: Role | None = Role.user
