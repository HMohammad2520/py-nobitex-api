from ._base import NobitexRoute

class Users(NobitexRoute):
    """
    Nobitex API Users endpoint.
    """
    _route_path: str = 'users'
    _version: str = ''

    def get_profile(self) -> dict:
        return self._client._send_request(
            'Get',
            route=self._create_route('profile')
        )