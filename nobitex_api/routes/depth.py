from nobitex_api.currency import Currency
from nobitex_api.type_hints import CurrencyAgainstMode
from ._base import NobitexRoute

"""
https://api.nobitex.ir/v2/depth/BTCIRT #Done
"""

class Depth(NobitexRoute):
    """
    Nobitex API Depth endpoint.
    """

    _route_path: str = 'depth'
    _version: str = 'v2'

    def get_depth(
            self, 
            currency: Currency,
            against: CurrencyAgainstMode = 'irt'
        ) -> dict:
        """
        Get market depth for a specific currency.

        Args:
            currency (Currency): The currency to get market depth for.
            against (CurrencyAgainstMode, optional): The currency to get market depth against. Defaults to 'irt'

        Returns:
            dict: The market depth for the specified currency.
        """

        return self._client._send_request(
            method='GET',
            route=self._create_route(currency.get(against)),
        )