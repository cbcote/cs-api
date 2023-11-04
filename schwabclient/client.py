import requests
from .exceptions import APIError
from .config import API_BASE_URL
from .models import MyResource

class APIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = self._create_session()

    def _create_session(self):
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {self.api_key}'})
        return session

    def _request(self, method, url, **kwargs):
        response = self.session.request(method, url, **kwargs)
        if not response.ok:
            raise APIError(f'API request failed with status code {response.status_code}: {response.text}')
        return response

    def _get(self, url, **kwargs):
        return self._request('GET', url, **kwargs)

    def _post(self, url, data=None, json=None, **kwargs):
        return self._request('POST', url, data=data, json=json, **kwargs)

    def _put(self, url, data=None, **kwargs):
        return self._request('PUT', url, data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request('DELETE', url, **kwargs)

    # Example resource operations
    def get_resource(self, resource_id):
        url = f'{API_BASE_URL}/resources/{resource_id}'
        response = self._get(url)
        return MyResource.parse(response.json())

    def create_resource(self, resource_data):
        url = f'{API_BASE_URL}/resources'
        response = self._post(url, json=resource_data)
        return MyResource.parse(response.json())

    def update_resource(self, resource_id, resource_data):
        url = f'{API_BASE_URL}/resources/{resource_id}'
        response = self._put(url, json=resource_data)
        return MyResource.parse(response.json())

    def delete_resource(self, resource_id):
        url = f'{API_BASE_URL}/resources/{resource_id}'
        response = self._delete(url)
        return response.ok
