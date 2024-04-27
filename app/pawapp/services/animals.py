from httpx import AsyncClient


class AnimalSerice:
    @staticmethod
    async def get_animals():
        async with AsyncClient() as client:
            return await client.get('http://127.0.0.1:8080/animals/')
