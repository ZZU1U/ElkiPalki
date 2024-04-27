import os
from httpx import AsyncClient
from .users import UserService

class WalksService:
    @staticmethod
    async def get_walks_for_animal(animal_id: int):
        async with AsyncClient() as client:
            return await client.get(f'{os.environ.get("server_url")}/walks/get', params={"animal_id": animal_id})

    @staticmethod
    async def get_all():
        async with AsyncClient() as client:
            return await client.get(f'{os.environ.get("server_url")}/walks/all')

    @staticmethod
    async def add(walk: dict):
        async with AsyncClient() as client:
            user_id = (await UserService.get_by_name(walk['user_name'])).json().get('id', None)
            print((await UserService.get_by_name(walk['user_name'])).json())
            del walk['user_name']
            walk['user_id'] = user_id
            print(walk)
            return await client.post(f'{os.environ.get("server_url")}/walks/add', json=walk)
