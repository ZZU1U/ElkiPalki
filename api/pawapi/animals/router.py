from fastapi import APIRouter
from sqlalchemy import select

from .models import Animal
from .schemas import AnimalRead, AnimalUpdate, AnimalCreate
from .ormschemas import AnimalRelRead
from ..db.annotations import gen_session
from ..user.auth.dependencies import user, superuser


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
async def delete_animal(animal_id: int, session: gen_session, super_user: superuser) -> AnimalRead:
    animal = await session.get(Animal, animal_id)

    await session.delete(animal)
    await session.commit()

    return animal


@router.put("/")
async def update_animal(animal: AnimalUpdate, session: gen_session, super_user: superuser) -> AnimalRead:
    await session.merge(Animal(**animal.dict()))
    await session.commit()

    return AnimalRead.model_validate(animal, from_attributes=True)


@router.post("/")
async def create_animal(animal: AnimalCreate, session: gen_session, super_user: superuser) -> AnimalRead:
    animal_model = Animal(**animal.dict())

    session.add(animal_model)
    await session.commit()

    return AnimalRead.model_validate(animal_model, from_attributes=True)
