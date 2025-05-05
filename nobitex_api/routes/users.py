from ._base import NobitexRoute

"""
https://api.nobitex.ir/users/profile #Done
https://api.nobitex.ir/users/wallets/generate-address
https://api.nobitex.ir/users/cards-add
https://api.nobitex.ir/users/accounts-add
https://api.nobitex.ir/users/limitations
https://api.nobitex.ir/users/wallets/list
https://api.nobitex.ir/users/wallets/balance
https://api.nobitex.ir/users/wallets/transactions/list?wallet=4159
https://api.nobitex.ir/users/wallets/deposits/list?wallet=4159
https://api.nobitex.ir/users/markets/favorite
https://api.nobitex.ir/users/wallets/withdraw
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
        return self._client._send_request(
            'Get',
            route=self._create_route('profile')
        )