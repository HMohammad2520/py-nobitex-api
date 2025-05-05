from ._base import NobitexRoute
from nobitex_api.currency import CurrencyEnum

"""
https://api.nobitex.ir/v2/trades/ #Done
"""

class Trades(NobitexRoute):
    """
    Nobitex API trades endpoint.
    """
    _route_path: str = 'trades'
    _version: str = 'v2'

    def get_trades(self, currency: CurrencyEnum) -> dict:
        """
        Get trades data for a specific currency.

        Args:
            Currency (CurrencyEnum): Currency to get trades data for.
        Returns:
            dict: trades data.
        """

        return self._client._send_request(
            request_method='GET',
            route=self._create_route(currency.value),
        )
