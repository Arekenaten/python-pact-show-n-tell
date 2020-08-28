import requests

class Fetcher(object):
    def __init__(self, base_uri: str):
        self.base_uri = base_uri

    def ask_provider_to_add(self, x: int, y: int):
        """Hit the provider's Add endpoint with two values"""
        uri = f'{self.base_uri}/add?x={x}&y={y}'
        response = requests.get(uri)
        if response.status_code == 404:
            return None

        return response.json()