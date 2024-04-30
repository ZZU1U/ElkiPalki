from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserBase(BaseModel):
    name: str
    phone: PhoneNumber


class UserRead(UserBase):
    id: int
    is_superuser: bool = False
    is_volunteer: bool = False


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    id: int
