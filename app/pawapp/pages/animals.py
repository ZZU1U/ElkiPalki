import httpx
import asyncio
from flet import ListView, Column

from pawapp.components.animal import Animal
from pawapp.services.animals import AnimalSerice


async def AnimalsView():
    animals = (await AnimalSerice.get_animals()).json()
    return ListView(map(lambda animal: Animal(animal), animals), spacing=10)
