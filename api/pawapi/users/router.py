from sqlalchemy import select
from pawapi.database import session_factory
from pawapi.enums import Role
from pawapi.models import User
from .schemas import UserRead, UserWrite
from fastapi import APIRouter

router = APIRouter(prefix='/users', tags=['users'])


@router.post("/is_admin")
async def is_admin(name: str):
    async with session_factory() as session:
        query = select(User).where(User.name == name)
        result = await session.execute(query)
        result = result.unique().one_or_none()
        print(result)
        return result


@router.post("/create_user")
async def create_user(user: UserWrite) -> UserRead:
    async with session_factory() as session:
        u = User(**user.dict())
        session.add(u)
        await session.commit()
        return u
