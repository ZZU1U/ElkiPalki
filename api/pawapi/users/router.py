from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pawapi.database import session_factory, get_session
from pawapi.enums import Role
from pawapi.models import User
from .schemas import UserRead, UserWrite
from fastapi import APIRouter, Depends

router = APIRouter(prefix='/users', tags=['users'])


@router.post("/get")
async def get(name: str, session: AsyncSession = Depends(get_session)):
    query = select(User).where(User.name == name)
    result = await session.execute(query)
    result = result.scalar_one_or_none()
    if result is None:
        return {'detail': 'User does not exist'}
    return result


@router.post("/create_user")
async def create_user(user: UserWrite, session: AsyncSession = Depends(get_session)):
    u = User(**user.dict())
    session.add(u)
    await session.commit()
    print(u)
    return u
