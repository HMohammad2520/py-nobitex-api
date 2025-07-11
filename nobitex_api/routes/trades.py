# nobitex_api\routes\trades.py
from ._base import NobitexRoute
from nobitex_api._currency import Currency
from nobitex_api._type_hints import CurrencyAgainstMode

"""
https://api.nobitex.ir/v2/trades/ #Done
"""

class Trades(NobitexRoute):
    """
    Nobitex API trades endpoint.
    """
    _route_path: str = 'trades'
    _version: str = 'v2'

    def get_trades(
            self, 
            currency: Currency,
            against: CurrencyAgainstMode = 'irt',
            ) -> dict:
        """
        Get trades data for a specific currency.

        Args:
            Currency (CurrencyEnum): Currency to get trades data for.
            against (CurrencyMode, optional): Currency to get trades data against. Defaults to 'irt'
        Returns:
            dict: trades data.
        """

        return self._client._send_request(
            method='GET',
            route=self._create_route(currency.get(against)),
        )
