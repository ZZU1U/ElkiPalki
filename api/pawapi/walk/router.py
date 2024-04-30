from fastapi import APIRouter, Depends
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Walk
from .schemas import WalkRead
from ..db.annotations import gen_session


router = APIRouter(prefix='/walk', tags=['walk'])


@router.get('/')
async def read_walks(session: gen_session) -> list[WalkRead]:
    query = (
        select(Walk)
    )

    result = await session.scalars(query)
    return result.scalars()


@router.delete('/{walk_id}')
async def delete_walk(walk_id: int, session: gen_session):
    walk = await session.get(Walk, walk_id)

    session.delete(walk)

    await session.commit()
