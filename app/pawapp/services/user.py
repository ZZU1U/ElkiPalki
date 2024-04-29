import requests

from .config import SERVER_URL
from .settings import Settings


class UserService:
    @staticmethod
    def register(name: str, email: str, password: str, phone_number: str | None = None) -> dict:
        data = {
            'name': name,
            'email': email,
            'password': password,
            'phone_number': phone_number
        }

        response = requests.post(f'{SERVER_URL}/auth/register', json=data)
        return response.json()

    @staticmethod
    def login(email: str, password: str):
        data = {
            'username': email,
            'password': password
        }
        response = requests.post(f'{SERVER_URL}/auth/login', data=data)
        token = response.json().get('access_token', None)
        Settings.write(token=token)
        return token

    @staticmethod
    def logout() -> str:
        headers = Settings.headers()
        response = requests.post(f'{SERVER_URL}/auth/logout', headers=headers)
        return response.json()

    @staticmethod
    def current() -> dict:
        response = requests.get(f'{SERVER_URL}/user')
        return response.json()
