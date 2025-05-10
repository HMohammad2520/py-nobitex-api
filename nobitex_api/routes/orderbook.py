# nobitex_api\routes\orderbook.py
from ._base import NobitexRoute
from nobitex_api._currency import Currency
from nobitex_api._type_hints import CurrencyAgainstMode

"""
https://api.nobitex.ir/v3/orderbook #Done
"""

class Orderbook(NobitexRoute):
    """
    Nobitex API Orderbook endpoint.
    """
    _route_path: str = 'orderbook'
    _version: str = 'v3'

    def get_orders(
            self, 
            currency: Currency,
            against: CurrencyAgainstMode = 'irt',
            ) -> dict:
        """
        Get orderbook data for a specific currency.

        Args:
            Currency (CurrencyEnum): Currency to get orderbook data for.
            against (CurrencyMode, optional): Currency to get orderbook data against. Defaults to 'irt'
        Returns:
            dict: Orderbook data.
        """

        return self._client._send_request(
            method='GET',
            route=self._create_route(currency.get(against)),
        )
