from pawapi.models import Walk, Animal
from pawapi.database import session_factory
from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import selectinload, Session
from .ormschemas import WalkRelRead, WalkRead

router = APIRouter(prefix='/walks', tags=['walks'])


@router.get('/get')
async def get_walks(animal_id: int) -> list[WalkRelRead]:
    async with session_factory() as session:
        query = select(Walk).where(Walk.animal_id == animal_id)
        return (await session.execute(query)).unique().scalars().all()


@router.get('/all')
async def get_all_walks() -> list[WalkRelRead]:
    async with session_factory() as session:
        query = select(Walk).options(
            selectinload(Walk.user),
            selectinload(Walk.animal),
        )
        res = (await session.execute(query)).unique().scalars().all()
        res = [WalkRelRead.model_validate(row, from_attributes=True) for row in res]
        return res
