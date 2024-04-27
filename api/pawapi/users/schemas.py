from pydantic import BaseModel
from pawapi.enums import Role


class UserBase(BaseModel):
    name: str
    role: Role | None = Role.user


class UserRead(UserBase):
    id: int


class UserWrite(UserBase):
    pass
