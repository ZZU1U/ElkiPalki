import os

from httpx import AsyncClient


class AdminService:
    @staticmethod
    async def is_admin(name: str) -> bool:
        async with AsyncClient() as client:
            response = await client.post(f'{os.environ.get("server_url")}/users/is_admin', params={"name": name})
            return bool(response.json().get('role'))

    @staticmethod
    async def change_animal(animal: dict) -> dict:
        async with AsyncClient() as client:
            response = await client.post(f'{os.environ.get("server_url")}/animals/change', json=animal)
            return response.json()
