from typing import List, Literal, Optional
from nobitex_api.currency import Currency
from nobitex_api.type_hints import CurrencyAgainstMode
from ._base import NobitexRoute

"""
https://api.nobitex.ir/v2/wallets #Done
https://api.nobitex.ir/wallets/transfer #Done
"""

class Wallets(NobitexRoute):
    """
    Nobitex API Wallets endpoint.
    """

    _route_path: str = 'wallets'
    _version: str = ''

    def get_wallet(
            self,
            type: Literal['spot', 'margin'],
            currencies: Optional[List[Currency]] = None,
        ) -> dict:
        """
        Get wallet information.

        Args:
            type (str): Type of wallet. It can be 'spot' or 'margin'.
            currencies (list, optional): List of currencies. Defaults to None.
        
        Returns:
            dict: Wallet information.
        """

        currencies_str: List[str] = [currency.symbol for currency in currencies] if currencies is not None else None
        get_parms = {
            'type': type,
            'currencies': ''.join(currencies_str, ',') if currencies_str is not None else None,
            }
        get_parms = {k: v for k, v in get_parms.items() if v is not None}

        return self._client._send_request(
            request_method='GET',
            route=self._create_route(version='v2'),
            get_parms=get_parms,
        )

    def transfer(
            self,
            currency: Currency,
            amount: float,
            src: Literal['spot', 'margin'],
            dst: Literal['spot', 'margin'],
        ) -> dict:
        """
        Transfer money between wallets.

        Args:
            currency (Currency): Currency of the transfer.
            amount (float): Amount of the transfer.
            src (str): Source wallet type. It can be 'spot' or 'margin'.
            dest (str): Destination wallet type. It can be 'spot' or 'margin'.

        Returns:
            dict: Transfer information.
        """

        post_parms = {
            'currency': currency.symbol,
            'amount': amount,
            'src': src,
            'dst': dst,
        }

        return self._client._send_request(
            request_method='POST',
            route=self._create_route('transfer'),
            post_parms=post_parms,
        )