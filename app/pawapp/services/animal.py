import requests

from .config import SERVER_URL
from .settings import Settings


class AnimalService:
    @staticmethod
    def read_all() -> list[dict]:
        response = requests.get(f'{SERVER_URL}/animals/')
        return response.json()

    @staticmethod
    def read(id: int) -> dict:
        response = requests.get(f'{SERVER_URL}/animals/{id}/')
        return response.json()

    @staticmethod
    async def create(animal: dict) -> dict:
        headers = Settings.headers()
        response = requests.post(f'{SERVER_URL}/animals/', json=animal, headers=headers)
        return response.json()

    @staticmethod
    async def update(animal: dict) -> dict:
        headers = Settings.headers()
        response = requests.put(f'{SERVER_URL}/animals/', json=animal, headers=headers)
        return response.json()