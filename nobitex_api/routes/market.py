from typing import Optional
from nobitex_api.type_hints import NobitexBool, NobitexCaptcha
from ._base import NobitexRoute

"""
https://api.nobitex.ir/market/orders/add 
https://api.nobitex.ir/market/orders/status 
https://api.nobitex.ir/market/orders/list 
https://api.nobitex.ir/market/orders/update-status 
https://api.nobitex.ir/market/orders/cancel-old 
https://api.nobitex.ir/market/trades/list 
https://api.nobitex.ir/market/stats 
https://api.nobitex.ir/market/udf/history 
https://api.nobitex.ir/market/global-stats 
"""

class Market(NobitexRoute):
    """
    Nobitex API Market endpoint.
    """

    _route_path: str = 'market'
    _version: str = ''

    def add_order(self) -> dict:
        """
        Add a new order.
        """
        raise NotImplementedError

    def get_order_status(self) -> dict:
        """
        Get the status of an order.
        """
        raise NotImplementedError

    def get_orders_list(self) -> dict:
        """
        Get the list of orders.
        """
        raise NotImplementedError

    def update_order_status(self) -> dict:
        """
        Update the status of an order.
        """
        raise NotImplementedError

    def cancel_old_orders(self) -> dict:
        """
        Cancel old orders.
        """
        raise NotImplementedError

    def get_trades_list(self) -> dict:
        """
        Get the list of trades.
        """
        raise NotImplementedError

    def get_stats(self) -> dict:
        """
        Get market stats.
        """
        raise NotImplementedError

    def get_udf_history(self) -> dict:
        """
        Get UDF history.
        """
        raise NotImplementedError

    def get_global_stats(self) -> dict:
        """
        Get global market stats.
        """
        raise NotImplementedError
