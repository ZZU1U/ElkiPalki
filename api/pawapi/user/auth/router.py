from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.exc import IntegrityError

from pawapi.db.annotations import gen_session
from ..schemas import UserCreate
from ..models import User
from .utils import get_access_token


router = APIRouter(prefix='/auth', tags=['user'])


@router.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    phone = data.username
    password = data.password

    access_token = await get_access_token(phone, password)

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/register')
async def register(user: UserCreate, session: gen_session):
    user_orm = User(**user.model_dump())
    try:
        session.add(user_orm)
        await session.commit()
    except IntegrityError as e:
        raise HTTPException(409, 'User already exists')
