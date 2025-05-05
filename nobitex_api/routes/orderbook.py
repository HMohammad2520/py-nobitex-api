from ._base import NobitexRoute
from nobitex_api.currency import CurrencyEnum

"""
https://api.nobitex.ir/v3/orderbook #Done
"""

class Orderbook(NobitexRoute):
    """
    Nobitex API Orderbook endpoint.
    """
    _route_path: str = 'orderbook'
    _version: str = 'v3'

    def get_orders(self, currency: CurrencyEnum) -> dict:
        """
        Get orderbook data for a specific currency.

        Args:
            Currency (CurrencyEnum): Currency to get orderbook data for.
        Returns:
            dict: Orderbook data.
        """

        return self._client._send_request(
            request_method='GET',
            route=self._create_route(currency.value),
        )
