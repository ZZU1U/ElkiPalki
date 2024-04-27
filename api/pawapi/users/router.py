from sqlalchemy import select
from pawapi.database import session_factory
from pawapi.enums import Role
from pawapi.models import User
from .schemas import UserRead
from fastapi import APIRouter

router = APIRouter(prefix='/users', tags=['animals'])


@router.post("/is_admin")
async def is_admin(name: str):
    async with session_factory() as session:
        query = select(User).where(User.name == name)
        result = await session.execute(query)
        result = result.unique().one_or_none()
        return {'detail': 'no admin found'} if result is None or result[0].role != Role.admin else result[0]
