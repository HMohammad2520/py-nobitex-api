# nobitex_api\routes\users.py
from typing import List, Literal, Optional
from nobitex_api._currency import Currency
from nobitex_api._type_hints import CurrencyAgainstMode
from ._base import NobitexRoute

"""
https://api.nobitex.ir/users/profile #Done
https://api.nobitex.ir/users/wallets/generate-address #Done
https://api.nobitex.ir/users/cards-add #Done
https://api.nobitex.ir/users/accounts-add #Done
https://api.nobitex.ir/users/limitations #Done
https://api.nobitex.ir/users/wallets/list #Done
https://api.nobitex.ir/users/wallets/balance #Done
https://api.nobitex.ir/users/wallets/transactions/list #Done
https://api.nobitex.ir/users/wallets/deposits/list #Done
https://api.nobitex.ir/users/markets/favorite #Done x3
https://api.nobitex.ir/users/wallets/withdraw #Done
https://api.nobitex.ir/users/wallets/withdraw-confirm
https://api.nobitex.ir/users/wallets/withdraws/list
https://api.nobitex.ir/users/get-referral-code
https://api.nobitex.ir/users/referral/referral-status
https://api.nobitex.ir/users/referral/set-referrer
https://api.nobitex.ir/users/referral/links-list
https://api.nobitex.ir/users/login-attempts
https://api.nobitex.ir/users/portfolio/last-week-daily-profit
https://api.nobitex.ir/users/portfolio/last-week-daily-total-profit
https://api.nobitex.ir/users/portfolio/last-month-total-profit
"""

class Users(NobitexRoute):
    """
    Nobitex API Users endpoint.
    """
    _route_path: str = 'users'
    _version: str = ''

    def get_profile(self) -> dict:
        """
        Get user profile information.

        Returns:
            dict: User profile information.
        """

        return self._client._send_request(
            method='Get',
            route=self._create_route('profile'),
        )
    
    def generate_wallet_address(
            self,
            currency: Currency,
            wallet: Optional[str] = None,
        ) -> dict:
        """
        Generate a new wallet address.

        Args:
            currency (Currency): Currency to generate wallet address for.
            wallet (Optional[str]): Wallet id to generate address for. Defaults to None.

        Returns:
            dict: Wallet address information.
        """

        post_parms = {
            'currency': currency.symbol,
            'wallet': wallet,
        }
        post_parms = {k: v for k, v in post_parms.items() if v is not None}

        return self._client._send_request(
            method='POST',
            route=self._create_route('wallets', 'generate-address'),
            post_parms=post_parms,
        )
    
    def add_card(
            self,
            number: str,
            bank: str,
        ) -> dict:
        """
        Add a new card.

        Args:
            number (str): Card number.
            bank (str): Bank name in persian (eg. 'رسالت').
        
        Returns:
            dict: Card information.
        """

        post_parms = {
            'number': number,
            'bank': bank,
        }
        return self._client._send_request(
            method='POST',
            route=self._create_route('cards-add'),
            post_parms=post_parms,
        )
    
    def add_account(
            self,
            number: str,
            shaba:str,
            bank: str,
        ) -> dict:
        """
        Add a new account.

        Args:
            number (str): Account number.
            shaba (str): Account shaba.
            bank (str): Bank name in persian (eg. 'رسالت').
        
        Returns:
            dict: Account information.
        """

        post_parms = {
            'number': number,
            'shaba': shaba,
            'bank': bank,
        }
        return self._client._send_request(
            method='POST',
            route=self._create_route('accounts-add'),
            post_parms=post_parms,
        )

    def get_limitations(
            self,
        ) -> dict:
        """
        Get limitations.

        Returns:
            dict: Limitations information.
        """
        return self._client._send_request(
            method='GET',
            route=self._create_route('limitations'),
        )

    def list_wallets(
            self,
            type: Literal['spot', 'margin'] = 'spot',
        ) -> dict:
        """
        List wallets.

        Args:
            type (Literal['spot', 'margin']): Wallet type.
        
        Returns:
            dict: Wallets information.
        """
        get_parms = {
            'type': type,
        }
        return self._client._send_request(
            method='GET',
            route=self._create_route('wallets', 'list'),
            get_parms=get_parms,
        )
    
    def get_wallet_balance(
            self,
            currency: Currency,
        ) -> dict:
        """
        Get wallet balance.

        Args:
            currency (Currency): Currency code.
        
        Returns:
            dict: Wallet balance information.
        """
        post_parms = {
            'currency': currency.symbol,
        }
        return self._client._send_request(
            method='POST',
            route=self._create_route('wallets', 'balance'),
            post_parms=post_parms,
        )
    
    def get_wallet_transactions(
            self,
            wallet_id: int,
        ) -> dict:
        """
        Get wallet transactions.

        Args:
            wallet_id (int): Currency code.
        
        Returns:
            dict: Wallet transactions information.
        """
        get_parms = {
            'wallet': wallet_id,
        }
        return self._client._send_request(
            method='GET',
            route=self._create_route('wallets', 'transactions', 'list'),
            get_parms=get_parms,
        )
    
    def get_wallet_deposits(
            self,
            wallet_id: int,
        ) -> dict:
        """
        Get wallet deposits.

        Args:
            wallet_id (int): Wallet ID.

        Returns:
            dict: Wallet deposits information.
        """
        get_parms = {
            'wallet': wallet_id,
        }
        return self._client._send_request(
            method='GET',
            route=self._create_route('wallets', 'deposits', 'list'),
            get_parms=get_parms,
        )
    
    def get_favorite_market(
            self,
        ) -> dict:
        """
        Get favorite market.

        Returns:
            dict: Favorite market information.
        """
        return self._client._send_request(
            method='GET',
            route=self._create_route('markets', 'favorite'),
        )
    
    def set_favorite_markets(
            self,
            markets: List[Currency],
            against: CurrencyAgainstMode,
        ) -> dict:
        """
        Set favorite markets.

        Args:
            markets (List[Currency]): List of markets to set as favorite.
            against (CurrencyAgainstMode): Market against mode.
        
        Returns:
            dict: Favorite markets information.
        """
        markets_str: List[str] = [currency.get(against) for currency in markets]

        post_parms = {
            'market': ','.join(markets_str),
        }
        return self._client._send_request(
            method='POST',
            route=self._create_route('markets', 'favorite'),
            post_parms=post_parms,
        )
    
    def delete_favorite_markets(
            self,
            markets: List[Currency],
            against: CurrencyAgainstMode,
        ) -> dict:
        """
        Delete favorite markets.

        Args:
            markets (List[Currency]): List of markets to delete from favorites.
            against (CurrencyAgainstMode): Market against mode.

        Returns:
            dict: Favorite markets information.
        """
        markets_str: List[str] = [currency.get(against) for currency in markets]
        post_parms = {
            'market': ','.join(markets_str),
            }
        return self._client._send_request(
            method='DELETE',
            route=self._create_route('markets', 'favorite'),
            post_parms=post_parms,
        )
    
    def add_wallet_withdraw(
            self,
            wallet_id: int,
            network: Optional[str] = None,
            invoice: Optional[str] = None,
            amount: Optional[str] = None,
            address: Optional[str] = None,
            explanations: Optional[str] = None,
            no_tag: Optional[bool] = None,
            tag: Optional[str] = None,
        ) -> dict:
        """
        Add a new wallet withdraw.

        Args:
            wallet_id (int): Wallet ID.
            network (Optional[str]): Network. Defaults to None.
            invoice (Optional[str]): Invoice. Defaults to None.
            amount (Optional[str]): Amount. Defaults to None.
            address (Optional[str]): Address. Defaults to None.
            explanations (Optional[str]): Explanations. Defaults to None.
            no_tag (Optional[bool]): No tag. Defaults to None.
            tag (Optional[str]): Tag. Defaults to None.

        Returns:
            dict: Withdraw information.
        """
        post_parms = {
            'wallet': wallet_id,
            'network': network,
            'invoice': invoice,
            'amount': amount,
            'address': address,
            'explanations': explanations,
            'noTag': no_tag,
            'tag': tag,
        }
        post_parms = {k: v for k, v in post_parms.items() if v is not None}

        return self._client._send_request(
            method='POST',
            route=self._create_route('wallets', 'withdraw'),
            post_parms=post_parms,
        )
    
