import requests
import json
import os

import dotenv


dotenv.load_dotenv()


BASE_URL=os.getenv('DJANGO_NINJA_EXAMPLE_ENDPOINT', 'http://localhost:8000')
API_TOKEN=os.getenv('DJANGO_NINJA_EXAMPLE_API_TOKEN')


def auth_headers():
    return {
        'Authorization': f'Token {API_TOKEN}'
    }



def pretty(response):
    return json.dumps(response.json(), indent=2)


def auth_test():
    url = f'{BASE_URL}/api/secret'
    response = requests.get(url)
    print('--- unauth test ---')
    print(response)
    url = f'{BASE_URL}/api/secret'
    response = requests.get(url, headers=auth_headers())
    print('--- auth test ---')
    print(pretty(response))


def create():
    url = f'{BASE_URL}/api/widget'
    with open('create-widget.json') as f:
        data = json.load(f)
    response = requests.post(url, headers=auth_headers(), json=data)
    print('--- create test ---')
    print(pretty(response))
    created_id = response.json()['id']
    with open('bad-create-widget.json') as f:
        data = json.load(f)
    response = requests.post(url, headers=auth_headers(), json=data)
    print('--- bad create test ---')
    print(pretty(response))
    return created_id


def read(created_id):
    url = f'{BASE_URL}/api/widget/{created_id}'
    response = requests.get(url)
    print('-- read test --')
    print(pretty(response))


def update(created_id):
    url = f'{BASE_URL}/api/widget/{created_id}'
    with open('update-widget.json') as f:
        data = json.load(f)
    response = requests.put(url, headers=auth_headers(), json=data)
    print('--- update test ---')
    print(pretty(response))


def delete(created_id):
    url = f'{BASE_URL}/api/widget/{created_id}'
    response = requests.delete(url, headers=auth_headers())
    print('--- delete test ---')
    print(pretty(response))


def list_widgets():
    url = f'{BASE_URL}/api/widgets'
    response = requests.get(url)
    print('--- list test ---')
    print(pretty(response))
    return response.json()


def clear_database():
    for widget in list_widgets():
        delete(widget['id'])


if __name__ == '__main__':
    auth_test()
    clear_database()
    created_id = create()
    read(created_id)
    list_widgets()
    update(created_id)
    list_widgets()
