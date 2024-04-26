import httpx
import asyncio
from flet import ListView
from pawapp.services.animals import AnimalSerice


class AnimalsView(ListView):
    async
        asyncio.run(self._init())
    async def _init(self):
        animals = await AnimalSerice.get_animals()
        print(animals)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        asyncio.run(self._init())

