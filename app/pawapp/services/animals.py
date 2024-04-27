import os
from httpx import AsyncClient


class AnimalService:
    @staticmethod
    async def get_animals():
        async with AsyncClient() as client:
            return await client.get(f'{os.environ.get("server_url")}/animals/')
