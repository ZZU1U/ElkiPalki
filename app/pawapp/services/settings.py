import json


def write_settings(token, id):
    with open('settings.json', 'w+') as f:
        json.dump({'token': token, 'id': id}, f)


def get_settings():
    try:
        with open('settings.json', 'r+') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'token': None, 'id': None}
