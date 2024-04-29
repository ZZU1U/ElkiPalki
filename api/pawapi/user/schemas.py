from fastapi_users import schemas
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    name: str
    phone: PhoneNumber | None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    is_volunteer: bool = False


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    name: str
    phone: PhoneNumber | None = None
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False
    is_volunteer: bool | None = False


class UserUpdate(schemas.BaseUserUpdate):
    pass  # UNUSED
