# nobitex_api\routes\options.py
from ._base import NobitexRoute

"""
https://api.nobitex.ir/v2/options #Done
"""

class Options(NobitexRoute):
    """
    Nobitex API Options endpoint.
    """
    _route_path: str = 'options'
    _version: str = 'v2'

    def get_options(
            self,
        ) -> dict:
        """
        Get options data.

        Returns:
            dict: Options data.
        """

        return self._client._send_request(
            method='GET',
            route=self._create_route(),
        )