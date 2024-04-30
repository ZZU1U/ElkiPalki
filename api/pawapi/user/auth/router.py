from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from werkzeug.security import generate_password_hash, check_password_hash

from pawapi.db.annotations import gen_session
from .manager import manager
from .database import load_user
from ..schemas import UserCreate
from ..models import User


router = APIRouter(prefix='/auth', tags=['user'])


@router.post('/auth/login')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    phone = data.username
    password = data.password

    user = await load_user(phone)
    if not user:
        raise InvalidCredentialsException
    elif check_password_hash(user.hashed_password, password):
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=phone)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/auth/register')
async def register(user: UserCreate, session: gen_session):
    user_orm = User(**user.model_dump())
    session.add(user_orm)

    await session.commit()
