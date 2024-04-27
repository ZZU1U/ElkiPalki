import json


def write_settings(**kwargs):
    with open('settings.json', 'w+') as f:
        json.dump(kwargs, f)


def get_settings():
    try:
        with open('settings.json', 'r+') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'token': None, 'id': None}
