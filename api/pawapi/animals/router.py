from pawapi.models import Animal
from .schemas import AnimalRead, AnimalChange
from fastapi import APIRouter

router = APIRouter(prefix='/animals', tags=['animals'])


@router.get("/")
async def get_animals() -> list[AnimalRead]:
    return await Animal.all()

@router.post("/change")
async def change_animal(animal: AnimalChange) -> AnimalRead:
    return await Animal.change(animal)
