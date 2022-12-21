import requests
from dataclasses import dataclass


@dataclass
class Response:
    status_code: int
    text: str
    json_dict: object
    headers: dict
    url: str


class ApiCall:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url, headers=''):
        return self._response_data(requests.get(self.base_url + url, headers))

    def post(self, url, payload, headers=''):
        return self._response_data(
            requests.post(url=(self.base_url + url), data=payload, headers=headers))

    def delete(self, url):
        return self._response_data(requests.delete(self.base_url + url))

    def put(self, url, payload, headers):
        return self._response_data(
            requests.put(url=(self.base_url + url), data=payload, headers=headers))

    @staticmethod
    def _response_data(response):
        status_code = response.status_code
        text = response.text
        headers = response.headers
        url = response.url

        try:
            json_dict = response.json()
        except Exception:
            json_dict = {}

        return Response(status_code, text, json_dict, headers, url)
