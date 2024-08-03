import os
import requests
from typing import Text, Dict

from pyserper.exceptions import MissingAPIKeyError


class SerperAPIClient:
    """
    Serper API client.
    """

    def __init__(self, api_key: Text = None):
        """
        Initialize the Serper API client.
        """
        self.api_key = self._get_api_key(api_key)

    def _get_api_key(self, api_key: Text = None) -> Text:
        """
        Get the API key.

        The API key can be provided as an argument or as the environment variable SERPER_API_KEY.

        :param api_key: API key.
        :return: API key.
        """
        if not api_key:
            api_key = os.environ.get('TWELVE_LABS_API_KEY', None)
        if not api_key:
            raise MissingAPIKeyError('API key must be provided.')
        return api_key
    
    def _get_headers(self, headers: Dict = {}) -> Dict:
        """
        Get the request headers. The API key and content type are added as headers and returned.

        :param headers: Request headers.
        :return: Headers.
        """
        headers['x-api-key'] = self.api_key
        headers['Content-Type'] = 'application/json'
        return headers
    
    def _get_url(self, endpoint: Text) -> Text:
        """
        Get the API URL.

        :param endpoint: API endpoint.
        :return: API URL.
        """
        # TODO: Move the base URL to settings.
        return f'https://google.serper.dev/{endpoint}'
    
    def submit_request(self, endpoint: str, headers: Dict = {}, data: Dict = {}) -> requests.Response:
        """
        Submit a request to the Serper API.

        :param endpoint: API endpoint.
        :param headers: Request headers. The API key and content type are automatically added.
        :param data: Request payload.
        :return: Response data.
        """
        url = self._get_url(endpoint)
        headers = self._get_headers(headers)

        response = requests.post(
            url=url,
            headers=headers,
            data=data,
        )

        return response