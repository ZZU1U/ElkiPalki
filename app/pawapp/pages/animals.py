import httpx
import asyncio
from flet import ListView, Column, Page
from ..components.appbar import MyAppBar
from ..components.animal import Animal
from ..services.animals import AnimalService


async def AnimalsView(page: Page, back=None):
    page.clean()
    page.appbar = MyAppBar('Наши животные', back=back)
    animals = (await AnimalService.get_animals()).json()
    page.add(ListView(list(map(lambda animal: Animal(animal, page=page, back=(lambda e: asyncio.run(AnimalsView(page, back)))), animals)), spacing=10))
