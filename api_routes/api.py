import requests

base_route = 'https://poetrydb.org'


def get_author():
    return requests.get(f'{base_route}/author').json()


def get_poem(poem):
    return requests.get(f'{base_route}/title/{poem}').json()


def get_line_author(line):
    return requests.get(f'{base_route}/lines/{line}/author').json()