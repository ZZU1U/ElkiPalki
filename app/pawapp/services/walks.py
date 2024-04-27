import os
from httpx import AsyncClient


class WalksService:
    @staticmethod
    async def get_walks(animal_id: int):
        async with AsyncClient() as client:
            return await client.get(f'{os.environ.get("server_url")}/walks/get', params={"animal_id": animal_id})
