from fastapi_login.exceptions import InvalidCredentialsException

from .database import load_user
from .manager import manager


async def get_access_token(phone: str, password: str) -> str:
    user = await load_user(phone)

    if not user:
        raise InvalidCredentialsException
    elif user.password != password:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=phone)
    )
    return access_token
