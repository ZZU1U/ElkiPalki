import os
from httpx import AsyncClient


class UserService:
    @staticmethod
    async def add_user(user: dict):
        async with AsyncClient() as client:
            return await client.post(f'{os.environ.get("server_url")}/users/create', data=user)

    @staticmethod
    async def get_by_name(name: str):
        async with AsyncClient() as client:
            return await client.post(f'{os.environ.get("server_url")}/users/get', params={'name': name})
