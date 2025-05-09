import json, requests_cache
from requests import Response, Session

from typing import Optional, Literal
from datetime import datetime, timedelta

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

        # Default session (non-cached)
        self._normal_session = Session()

        # Cache settings
        self._caching = False
        self._cached_session: Optional[requests_cache.CachedSession] = None
        self._expire_after: Optional[timedelta | int] = None

        super().__init__()

    def enable_caching(
        self,
        backend: Literal["sqlite", "filesystem", "redis", "mongodb"] = "sqlite",
        expire_after: Optional[timedelta | int] = timedelta(hours=24),
        cache_name: Optional[str] = "nobitex_cache",
        connection: Optional[str] = None,
        **backend_options,
    ) -> None:
        """
        Enables caching with full configuration.

        Args:
            backend: Cache backend to use.
            expire_after: Expiration time for cache.
            cache_name: Filename or namespace.
            connection: URI string for Redis or MongoDB.
            backend_options: Extra args passed to backend (like `use_cache_dir=False`)
        """

        self._expire_after = expire_after

        if backend == "sqlite":
            self._cached_session = requests_cache.CachedSession(
                cache_name=f"{cache_name}.sqlite",
                backend="sqlite",
                expire_after=expire_after,
                **backend_options,
            )

        elif backend == "filesystem":
            self._cached_session = requests_cache.CachedSession(
                cache_name=cache_name,
                backend="filesystem",
                expire_after=expire_after,
                **backend_options,
            )

        elif backend == "redis":
            if not connection:
                raise ValueError("Redis URI is required for Redis backend.")
            self._cached_session = requests_cache.CachedSession(
                backend="redis",
                connection=connection,
                expire_after=expire_after,
                **backend_options,
            )

        elif backend == "mongodb":
            if not connection:
                raise ValueError("MongoDB URI is required for MongoDB backend.")
            self._cached_session = requests_cache.CachedSession(
                backend="mongodb",
                connection=connection,
                expire_after=expire_after,
                **backend_options,
            )

        else:
            raise ValueError(f"Unsupported backend: {backend}")

        self._caching = True

    def disable_caching(self, clear_cache: bool = True) -> None:
        """
        Disable caching.

        Args:
            clear_cache (bool, optional): Whether to clear the cache before disabling it. Defaults to True
        """

        if self._cached_session and clear_cache:
            self._cached_session.cache.clear()
        self._cached_session = None
        self._caching = False

    def clear_cache(self, time: Optional[timedelta | int] = None) -> None:
        """
        Clear the cache.
        If time is provided, clear the cache for requests made within the specified time frame.

        Args:
            time (Optional[timedelta | int], optional): Time frame to clear the cache for.
            Defaults to None.
        """

        if not isinstance(self._cached_session, requests_cache.CachedSession):
            return

        backend = self._cached_session.cache

        if time is None:
            backend.clear()
            if self._verbose:
                print("Cache cleared (all entries).")
        else:
            if isinstance(time, int):
                time = timedelta(seconds=time)

            cutoff = datetime.now() - time
            removed = 0

            for key, response in backend.responses.items():
                created = response.created_at
                if created and created < cutoff:
                    backend.delete(key)
                    removed += 1

            if self._verbose:
                print(f"Removed {removed} expired cache entries.")

    def _send_request(
            self, 
            method: RequestMethod,
            route: Optional[str] = '',
            head_parms: Optional[dict] = None,
            get_parms: Optional[dict] = None,
            post_parms: Optional[dict] = None,
            use_caching: Optional[bool] = False,
            expire_after: Optional[timedelta | int] = None,
        ) -> dict:
        """
        Send a request to the Nobitex API and return the response data.

        Args:
            request_method (RequestMethod): The HTTP method for the request ('GET', 'POST', etc.).
            route (str): The API route for the request.
            head_parms (dict): The headers for the request.
            get_parms (dict): The GET parameters for the request.
            post_parms (dict): The POST parameters for the request.
            use_caching (bool): Whether to use caching for the request. Defaults to False.
            expire_after (timedelta | int): Time frame to clear the cache for. Defaults to None

        Returns:
            dict: json data from the response as a dict.

        Raises:
            NobitexException: If the server returns an error response.
        """

        head_parms = head_parms or {}
        get_parms = get_parms or {}
        post_parms = post_parms or {}

        # Default parms
        head_parms['Content-Type'] = 'application/json'
        if self._token:
            head_parms['Authorization'] = f'Token {self._token}'

        route = f'/{route}' if route and not route.startswith('/') else route
        url = self._api_url + route
        session = self._cached_session if (self._caching and use_caching) else self._normal_session

        request_kwargs = {
            'method': method,
            'url': url,
            'headers': head_parms,
            'params': get_parms,
            'json': post_parms,
            'verify': True,
        }
        if use_caching and expire_after:
            request_kwargs['expire_after'] = expire_after

        response: Response = session.request(**request_kwargs)

        if self._verbose:
            from_cache = getattr(response, 'from_cache', False)
            print(f'Sending Request: {method} - {response.url} - {response.status_code} - Cache: {from_cache}')
            print(response.text)

        # Check for Server respond
        if 200 <= response.status_code < 500:
            response_dict: dict = json.loads(response.text)

        else:
            # Raise on server side http error
            response.raise_for_status()

        # Initiate server response
        if not 200 <= response.status_code < 300:
            raise NobitexException(f"Code: {response.status_code} --> Response:{response_dict}")

        return response_dict


    def __repr__(self):
        return f'{self.__class__.__name__}(username={self._username}, ***)'

    def __str__(self) -> str:
        return f'<{self.__class__.__name__} {self._username}>'
