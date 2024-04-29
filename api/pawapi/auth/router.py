from fastapi import APIRouter

from fastapi_users import FastAPIUsers

from .backend import auth_backend
from .manager import get_user_manager
from .models import User
from .schemas import UserRead, UserCreate


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(prefix='/auth', tags=['auth'])

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend)
)
