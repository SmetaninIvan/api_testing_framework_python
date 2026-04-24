import requests


class BaseClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, path: str, params=None):
        return requests.get(f"{self.base_url}{path}", headers=self.headers, params=params)
