from typing import Any, Optional

BASE_LIMIT = 300
BASE_OFFSET = 0

class NobitexRoute:
    """
    A base class for interacting with a Sarv CRM module. This class provides methods to 
    create, read, update, delete, and manage relationships of records in a module.
    
    Attributes:
        _module_name (str): The name of the module.
        _label_en (str): The label of the module in English.
        _label_pr (str): The label of the module in Persian.
        _client (SarvClient): The client instance used to send requests to the Sarv CRM API.
    """
    _route_path: str = ''
    _version: str = ''

    def _create_route(self, *addition: str) -> str:
        return f"{(f'/{self._version}' if self._version else '')}/{self._route_path}/{'/'.join(addition)}"

    def __init__(self, _client):
        """
        Initializes the SarvModule instance with a given client.

        Args:
            _client (NobitexClient): The client used for making API requests to Nobitex.
        """
        from nobitex_api import NobitexClient
        self._client: NobitexClient = _client

    def __repr__(self) -> str:
        """
        Returns a string representation of the NobitexRoute instance.

        Returns:
            str: A string representation of the NobitexRoute instance.
        """
        return f'{self.__class__.__name__}(client: SarvClient)'

    def __str__(self) -> str:
        """
        Returns a string that describes the NobitexRoute instance.

        Returns:
            str: A description of the NobitexRoute instance.
        """
        return f'<NobitexRoute {self._route_path}>'
