import httpx
import asyncio
from flet import ListView, Column

from pawapp.components.animal import Animal
from pawapp.services.animals import AnimalService


async def AnimalsView():
    animals = (await AnimalService.get_animals()).json()
    return ListView(list(map(lambda animal: Animal(animal), animals)), spacing=10)
