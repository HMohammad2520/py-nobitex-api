from typing import Optional
from nobitex_api.type_hints import NobitexBool, NobitexCaptcha
from ._base import NobitexRoute

"""
https://api.nobitex.ir/auth/login/ #Done
https://api.nobitex.ir/auth/logout/ #Done
https://api.nobitex.ir/auth/ws/token/ #Done
"""

class Auth(NobitexRoute):
    """
    Nobitex API Auth endpoint.
    """
    _route_path: str = 'auth'
    _version: str = ''

    def login(
            self, 
            username: Optional[str] = None, 
            password: Optional[str] = None, 
            remember: NobitexBool = 'no', 
            captcha: NobitexCaptcha = 'api',
            ) -> str:
        """
        Authenticate the user and retrieve an access token.

        Returns:
            str: The access token for authenticated requests.
        """
        post_parms = {
            'username': username or self._client._username,
            'password': password or self._client._password,
            'remember': remember,
            'captcha': captcha,
            }

        if not post_parms['username'] or not post_parms['password']:
            raise ValueError('Username and password are required')

        data = self._client._send_request(
            request_method = 'POST',
            route = self._create_route('login', ''), # Ensures Addition of / at the end
            post_parms = post_parms,
        )

        if data:
            self._client._token = data.get('key')
            self._client._device = data.get('device')
        
        return self._client._token

    def logout(self) -> None:
        """
        Clears the access token from the instance.

        This method should be called to invalidate the session.
        """
        if self._client._token:
            self._client._token = ''

        self._client._send_request(
            request_method = 'POST',
            route = self._create_route('logout', ''), # Ensures Addition of / at the end
        )

    def get_web_socket_token(self) -> str:
        """
        Retrieves the web socket token.
        """

        return self._client._send_request(
            request_method='GET',
            route=self._create_route('ws', 'token', ''), # Ensures Addition of / at the end
        ).get('token')