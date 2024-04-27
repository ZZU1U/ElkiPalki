from pawapi.models import Animal
from .schemas import AnimalRead
from fastapi import APIRouter

router = APIRouter(prefix='/animals', tags=['animals'])


@router.get("/")
async def get_animals() -> list[AnimalRead]:
    return await Animal.all()
