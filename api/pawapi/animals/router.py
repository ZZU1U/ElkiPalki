from fastapi import APIRouter
from sqlalchemy import select

from .models import Animal
from .schemas import AnimalRead, AnimalUpdate
from .ormschemas import AnimalRelRead
from ..db.annotations import gen_session


router = APIRouter(prefix='/animals', tags=['animals'])


@router.get("/")
async def read_animals(session: gen_session) -> list[AnimalRead]:
    query = select(Animal)

    result = await session.scalars(query)

    return result


@router.get("/{animal_id}")
async def read_animal_by_id(animal_id: int, session: gen_session) -> AnimalRelRead:
    animal = await session.get(Animal, animal_id)

    return animal


@router.delete("/{animal_id}")
async def delete_animal(animal_id: int, session: gen_session) -> AnimalRead:
    animal = await session.get(Animal, animal_id)

    await session.delete(animal)
    await session.commit()

    return animal


@router.put("/")
async def update_animal(animal: AnimalUpdate, session: gen_session) -> AnimalRead:
    await session.merge(Animal(**animal.dict()))
    await session.commit()

    return AnimalRead.model_validate(animal)
