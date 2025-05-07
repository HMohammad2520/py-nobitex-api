import json
from requests import Response, request
from typing import Optional

from ._mixins import RouteMixin
from ._url import NobitexAPI
from .exceptions import NobitexException
from .type_hints import RequestMethod

class NobitexClient(RouteMixin):
    """
    NobitexClient provides methods for interacting with the Nobitex API. 
    It supports authentication, data retrieval, and other API functionalities.
    """

    def __init__(
            self,
            username: Optional[str] = '',
            password: Optional[str] = '',
            token: Optional[str] = '',
            api_url: str = NobitexAPI,
            verbose: bool = False,
            ) -> None:
        """
        Initialize the NobitexClient.

        Args:
            username (str): The username for authentication.
            password (str): The password for authentication.
            api_url (str): URL of the Nobitex API, if you dont use the cloud version specify the local server.
            verbose (bool): Prints the response from the API. Defaults to False. Not Recommended
        """

        if not ((username and password) or token):
            raise ValueError("You must provide either a username and password or a token.")

        self._username = username
        self._password = password
        self._token = token
        self._api_url = api_url
        self._verbose = verbose

        self._device: str = ''

        super().__init__()


    def _send_request(
            self, 
            request_method: RequestMethod,
            route: Optional[str] = '',
            head_parms: Optional[dict] = None,
            get_parms: Optional[dict] = None,
            post_parms: Optional[dict] = None,
            ) -> dict:
        """
        Send a request to the Nobitex API and return the response data.

        Args:
            request_method (RequestMethod): The HTTP method for the request ('GET', 'POST', etc.).
            route (str): The API route for the request.
            head_parms (dict): The headers for the request.
            get_parms (dict): The GET parameters for the request.
            post_parms (dict): The POST parameters for the request.

        Returns:
            dict: json data from the response as a dict.

        Raises:
            NobitexException: If the server returns an error response.
        """

        head_parms = head_parms or {}
        get_parms = get_parms or {}
        post_parms = post_parms or {}

        # Default Header
        head_parms['Content-Type'] = 'application/json'

        if self._token:
            head_parms['Authorization'] = f'Token {self._token}'

        if route:
            route = route if route.startswith('/') else f'/{route}'

        url = self._api_url + route

        response: Response = request(
            method = request_method,
            url = url,
            params = get_parms,
            headers = head_parms,
            json = post_parms,
            verify = True,
            )

        # Print Verbose
        if self._verbose:
            print (f'Sending Request: {request_method} {response.url} --> {response.status_code} --> {response.text}')

        # Check for Server respond
        if 200 <= response.status_code < 500:
            response_dict: dict = json.loads(response.text)

        else:
            # Raise on server side http error
            response.raise_for_status()

        # Initiate server response
        if not 200 <= response.status_code < 300:
            raise NobitexException(
                f"Code: {response.status_code} --> Response:{response_dict}"
            )

        else:
            return response_dict


    def __repr__(self):
        """
        Provides a string representation for debugging purposes.

        Returns:
            str: A string containing the class name and key attributes.
        """
        return f'{self.__class__.__name__}(username={self._username}, ***)'

    def __str__(self) -> str:
        """
        Provides a human-readable string representation of the instance.

        Returns:
            str: A simplified string representation of the instance.
        """
        return f'<{self.__class__.__name__} {self._username}>'
