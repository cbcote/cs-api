import requests
from .exceptions import APIError
from .config import API_BASE_URL
from .models import MyResource

class APIClient:
    def __init__(self, api_key: str):
        """
        Initializes a new instance of the APIClient class.
        
        Args:
            api_key (str): The API key to use for authentication.
        """
        self.api_key = api_key
        self.session = self._create_session()

    def _create_session(self):
        """
        Creates a new requests session with the appropriate headers.
        
        Returns:
            requests.Session: The requests session.
        """
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {self.api_key}'})
        return session

    def _request(self, method, url, **kwargs):
        """
        Makes an API request.
        
        Args:
            method (str): The HTTP method to use.
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request.
        
        Returns:
            requests.Response: The response object.
        """
        response = self.session.request(method, url, **kwargs)
        if not response.ok:
            raise APIError(f'API request failed with status code {response.status_code}: {response.text}')
        return response

    def _get(self, url, **kwargs):
        """
        Makes a GET request.
        
        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request.
        
        Returns:
            requests.Response: The response object.
        """
        return self._request('GET', url, **kwargs)

    def _post(self, url, data=None, json=None, **kwargs):
        """
        Makes a POST request.
        
        Args:
            url (str): The URL to request.
            data (Optional[Dict[str, Any]]): The data to send in the request body.
            json (Optional[Dict[str, Any]]): The JSON data to send in the request body.
            **kwargs: Additional keyword arguments to pass to the request.
        
        Returns:
            requests.Response: The response object.
        """
        return self._request('POST', url, data=data, json=json, **kwargs)

    def _put(self, url, data=None, **kwargs):
        """
        Makes a PUT request.
        
        Args:
            url (str): The URL to request.
            data (Optional[Dict[str, Any]]): The data to send in the request body.
            **kwargs: Additional keyword arguments to pass to the request.
        
        Returns:
            requests.Response: The response object.
        """
        return self._request('PUT', url, data=data, **kwargs)

    def _delete(self, url, **kwargs):
        """
        Makes a DELETE request.
        
        Args:
            url (str): The URL to request.
            **kwargs: Additional keyword arguments to pass to the request.
        
        Returns:
            requests.Response: The response object.
        """
        return self._request('DELETE', url, **kwargs)

    def get_resource(self, resource_id):
        """
        Gets a resource by its ID.
        
        Args:
            resource_id (int): The ID of the resource to get.
        
        Returns:
            MyResource: The resource.
        """
        url = f'{API_BASE_URL}/resources/{resource_id}'
        response = self._get(url)
        return MyResource.parse(response.json())

    def create_resource(self, resource_data):
        """
        Creates a new resource.
        
        Args:
            resource_data (Dict[str, Any]): The data for the resource.
        
        Returns:
            MyResource: The resource.
        """
        url = f'{API_BASE_URL}/resources'
        response = self._post(url, json=resource_data)
        return MyResource.parse(response.json())

    def update_resource(self, resource_id, resource_data):
        """
        Updates an existing resource.
        
        Args:
            resource_id (int): The ID of the resource to update.
            resource_data (Dict[str, Any]): The data for the resource.
        
        Returns:
            MyResource: The resource.
        """
        url = f'{API_BASE_URL}/resources/{resource_id}'
        response = self._put(url, json=resource_data)
        return MyResource.parse(response.json())

    def delete_resource(self, resource_id):
        """
        Deletes a resource by its ID.
        
        Args:
            resource_id (int): The ID of the resource to delete.
        
        Returns:
            bool: True if the resource was deleted, False otherwise.
        """
        url = f'{API_BASE_URL}/resources/{resource_id}'
        response = self._delete(url)
        return response.ok
