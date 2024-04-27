import httpx
import asyncio
from flet import ListView, Column, Page

from ..components.appbar import MyAppBar
from ..components.animal import Animal
from ..services.animals import AnimalService


async def AnimalsView(page: Page, back=None):
    await page.clean_async()
    page.appbar = MyAppBar('Наши животные', back=back)
    animals = (await AnimalService.get_animals()).json()
    await page.add_async(ListView(list(map(lambda animal: Animal(animal), animals)), spacing=10))
