from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    name: str
    phone: str | None
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    is_volunteer: bool = False


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    name: str
    phone: str | None
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False
    is_volunteer: bool | None = False


class UserUpdate(schemas.BaseUserUpdate):
    pass  # UNUSED
