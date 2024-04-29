import json
import os


class Settings:
    @staticmethod
    def init():
        if not os.path.exists('settings.json'):
            with open('settings.json', 'w') as f:
                json.dump({}, f)

    @staticmethod
    def token() -> str:
        with open('settings.json', 'r') as f:
            return json.load(f).get('token', '')

    @staticmethod
    def headers():
        token = Settings.token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return headers

    @staticmethod
    def write(**kwargs) -> None:
        with open('settings.json', 'w+') as f:
            json.dump(kwargs, f)

    @staticmethod
    def read() -> dict:
        with open('settings.json', 'r+') as f:
            return json.load(f)

    @staticmethod
    def clear() -> None:
        with open('settings.json', 'w+') as f:
            f.write('')
