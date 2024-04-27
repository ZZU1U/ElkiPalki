from sqlalchemy.ext.asyncio import AsyncSession

from pawapi.models import Animal
from .ormschemas import AnimalRelRead, AnimalChange, AnimalRead
from ..database import get_session
from fastapi import APIRouter, Depends

router = APIRouter(prefix='/animals', tags=['animals'])


@router.get("/")
async def get_animals() -> list[AnimalRead]:
    res = await Animal.all()
    return [AnimalRead.model_validate(row, from_attributes=True) for row in res]


@router.post("/change")
async def change_animal(animal: AnimalChange) -> AnimalRead:
    return await Animal.change(animal)
