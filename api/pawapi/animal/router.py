from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from .models import Animal
from .schemas import AnimalRead, AnimalUpdate, AnimalCreate
from .ormschemas import AnimalRelRead
from ..db.annotations import gen_session
from ..user.auth.manager import current_user


router = APIRouter(prefix='/animal', tags=['animal'])


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
async def delete_animal(animal_id: int, session: gen_session, user: current_user) -> AnimalRead:
    if not user.is_superuser:
        raise HTTPException(403, 'You do not enough permissions.')

    animal = await session.get(Animal, animal_id)

    await session.delete(animal)
    await session.commit()

    return animal


@router.put("/")
async def update_animal(animal: AnimalUpdate, session: gen_session, user: current_user) -> AnimalRead:
    if not user.is_superuser:
        raise HTTPException(403, 'You do not enough permissions.')

    await session.merge(Animal(**animal.model_dump()))
    await session.commit()

    return AnimalRead.model_validate(animal, from_attributes=True)


@router.post("/")
async def create_animal(animal: AnimalCreate, session: gen_session, user: current_user) -> AnimalRead:
    if not user.is_superuser:
        raise HTTPException(403, 'You do not enough permissions.')

    animal_model = Animal(**animal.model_dump())

    session.add(animal_model)
    await session.commit()

    return AnimalRead.model_validate(animal_model, from_attributes=True)
