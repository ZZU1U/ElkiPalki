from sqlalchemy.ext.asyncio import AsyncSession
from pawapi.models import Walk, Animal
from pawapi.database import session_factory, get_session
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload, Session
from .ormschemas import WalkRelRead, WalkRead

router = APIRouter(prefix='/walks', tags=['walks'])


@router.get('/get')
async def get_walks(animal_id: int, session: AsyncSession = Depends(get_session)) -> list[WalkRelRead]:
    query = select(Walk).where(Walk.animal_id == animal_id)
    return (await session.execute(query)).unique().scalars().all()


@router.get('/all')
async def get_all_walks(session: AsyncSession = Depends(get_session)) -> list[WalkRelRead]:
    query = select(Walk).options(
        selectinload(Walk.user),
        selectinload(Walk.animal),
    )
    res = (await session.execute(query)).unique().scalars().all()
    res = [WalkRelRead.model_validate(row, from_attributes=True) for row in res]
    return res
