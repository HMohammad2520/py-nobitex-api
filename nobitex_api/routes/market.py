from typing import Literal, Optional
from nobitex_api.currency import Currency
from nobitex_api.type_hints import CurrencyAgainstMode
from ._base import NobitexRoute

"""
https://api.nobitex.ir/market/orders/add #Done
https://api.nobitex.ir/market/orders/status #Done
https://api.nobitex.ir/market/orders/list #Done
https://api.nobitex.ir/market/orders/update-status #Done
https://api.nobitex.ir/market/orders/cancel-old #Done
https://api.nobitex.ir/market/trades/list #Done
https://api.nobitex.ir/market/stats #Done
https://api.nobitex.ir/market/udf/history #Done
https://api.nobitex.ir/market/global-stats #Done
"""

class Market(NobitexRoute):
    """
    Nobitex API Market endpoint.
    """

    _route_path: str = 'market'
    _version: str = ''

    def add_order(
            self,
            type: Literal['buy', 'sell'],
            src_currency: Currency,
            dst_currency: Currency,
            amount: str,
            price: str,
            mode: Optional[Literal['oco']] = None,
            client_order_id: Optional[str] = None,
            stop_price: Optional[float] = None,
            stopLimitPrice: Optional[float] = None,
            execution: Literal['market', 'limit', 'stop_market', 'stop_limit'] = 'limit',
        ) -> dict:
        """
        Add a new order.

        Args:
            type: Type of order. Can be 'buy' or 'sell'.
            src_currency: Source currency of the order.
            dst_currency: Destination currency of the order.
            amount: Amount of the order.
            price: Price of the order.
            mode: Optional. Mode of the order. Can be 'oco'.
            client_order_id: Optional. Client order id.
            stop_price: Optional. Stop price of the order.
            stopLimitPrice: Optional. Stop limit price of the order.
            execution: Optional. Execution type of the order. Can be 'market', 'limit', 'stop_market', 'stop_limit'.

        Returns:
            dict: Response of the API.
        """
        post_parameters = {
            'type': type,
            'srcCurrency': src_currency.get('symbol'),
            'dstCurrency': dst_currency.get('symbol'),
            'amount': amount,
            'price': price,
            'mode': mode,
            'clientOrderId': client_order_id,
            'stopPrice': stop_price,
            'stopLimitPrice': stopLimitPrice,
            'execution': execution,
        }
        post_parameters = {k: v for k, v in post_parameters.items() if v is not None}

        return self._client._send_request(
            method = 'POST', 
            route = self._create_route('orders', 'add'),
            post_parms = post_parameters,
        )

    def get_order_status(
            self,
            id: int,
            client_order_id: Optional[str] = None,
        ) -> dict:
        """
        Get the status of an order.

        Args:
            id: Id of the order.
            client_order_id: Optional. Client order id.

        Returns:
            dict: Response of the API.
        """
        post_params = {
            'id': id,
            'clientOrderId': client_order_id,
        }
        post_params = {k: v for k, v in post_params.items() if v is not None}

        return self._client._send_request(
            method = 'POST',
            route = self._create_route('orders', 'status'),
            post_parms = post_params,
        )

    def get_orders_list(
            self,
            type: Literal['buy', 'sell'],
            trade_type: Literal['spot', 'margin'],
            src_currency: Currency,
            dst_currency: Currency,
            details: Literal[1, 2] = 1,
            from_id: int = 1,
            order: Optional[Literal['id', 'created_at', 'price']] = None,
            execution: Literal['market', 'limit', 'stop_market', 'stop_limit'] = 'limit',
            status: Literal['all', 'open', 'done', 'close'] = 'open',
        ) -> dict:
        """
        Get the list of orders.

        Args:
            type: Type of the order.
            trade_type: Type of the trade.
            src_currency: Source currency.
            dst_currency: Destination currency.
            details: Details level of the order.
            from_id: Fetch reults after this ID.
            order: Order of the fetched result.
            execution: Execution type of the order.
            status: Filter by status of the order.
            
        Returns:
            dict: Response of the API.
        """
        post_params = {
            'type': type,
            'tradeType': trade_type,
            'srcCurrency': src_currency.symbol,
            'dstCurrency': dst_currency.symbol,
            'details': details,
            'fromId': from_id,
            'order': order,
            'execution': execution,
            'status': status,
        }
        post_params = {k: v for k, v in post_params.items() if v is not None}

        return self._client._send_request(
            method = 'GET',
            route = self._create_route('orders', 'list'),
            post_parms = post_params,
        )

    def update_order_status(
            self,
            status: Literal['active', 'canceled'],
            order_id: int = None,
            clint_order_id: Optional[str] = None,
        ) -> dict:
        """
        Update the status of an order.

        Args:
        status: Status of the order.
        order_id: Order id.
        clint_order_id: Client order id.
        """
        
        post_params = {
            'status': status,
            'order': order_id,
            'clientOrderId': clint_order_id
        }
        post_params = {k: v for k, v in post_params.items() if v is not None}

        return self._client._send_request(
            method = 'POST',
            route = self._create_route('orders', 'update-status'),
            post_parms = post_params,
        )

    def cancel_old_orders(
            self,
            hours: float,
            execution: Optional[Literal['market', 'limit', 'stop_market', 'stop_limit']] = None,
            trade_type: Optional[Literal['margin', 'spot']] = None,
            src_currency: Optional[Currency] = None,
            dst_currency: Optional[Currency] = None,
        ) -> dict:
        """
        Cancel old orders.

        Args:
            hours: Hours to cancel orders.
            execution: Execution type.
            trade_type: Trade type.
            src_currency: Source currency.
            dst_currency: Destination currency.

        Returns:
            dict: Response from the server.
        """
        
        post_params = {
            'hours': hours,
            'execution': execution,
            'tradeType': trade_type,
            'srcCurrency': src_currency.symbol if src_currency is not None else None ,
            'dstCurrency': dst_currency.symbol if dst_currency is not None else None,
        }
        post_params = {k: v for k, v in post_params.items() if v is not None}
        
        return self._client._send_request(
            method = 'POST',
            route = self._create_route('orders', 'cancel-old'),
            post_parms = post_params,
        )

    def get_trades_list(
            self,
            src_currency: Optional[Currency] = None,
            dst_currency: Optional[Currency] = None,
            from_id : Optional[int] = None,
        ) -> dict:
        """
        Get the list of trades.

        Args:
            src_currency: Source currency.
            dst_currency: Destination currency.
            from_id: From id.

        Returns:
            dict: Response from the server.
        """

        get_parms = {
            'srcCurrency': src_currency.symbol if src_currency is not None else None,
            'dstCurrency': dst_currency.symbol if dst_currency is not None else None,
            'fromId': from_id,
        }
        get_parms = {k: v for k, v in get_parms.items() if v is not None}

        return self._client._send_request(
            method='GET',
            route=self._create_route('trades', 'list'),
            get_parms=get_parms,
        )

    def get_stats(
            self,
            src_currency: Optional[Currency] = None,
            dst_currency: Optional[Currency] = None,
        ) -> dict:
        """
        Get market stats.

        Args:
            src_currency: Source currency.
            dst_currency: Destination currency.

        Returns:
            dict: Response from the server.
        """

        get_parms = {
            'srcCurrency': src_currency.symbol if src_currency is not None else None,
            'dstCurrency': dst_currency.symbol if dst_currency is not None else None,
        }
        get_parms = {k: v for k, v in get_parms.items() if v is not None}
        
        return self._client._send_request(
            method='GET',
            route=self._create_route('stats'),
            get_parms=get_parms,
        )

    def get_udf_history(
            self,
            symbol: Currency,
            against: CurrencyAgainstMode,
            resolution: Literal['1', '5', '15', '30','60', '180', '240', '360', '720', 'D','2D', '3D'],
            to: int,
            fr: int = None,
            count_back: int = None,
            page: int = None,
            ) -> dict:
        """
        Get UDF history.

        Args:
            symbol: Symbol.
            resolution: Resolution.
            to: To timestamp.
            fr: From timestamp.
            count_back: Count back.
            page: Page number.
        
        Returns:
            dict: Response from the server.
        """
        get_parms = {
            'symbol': symbol.get(against),
            'resolution': resolution,
            'to': to,
            'from': fr,
            'countBack': count_back,
            'page': page,
            }
        get_parms = {k: v for k, v in get_parms.items() if v is not None}

        return self._client._send_request(
            method='GET',
            route=self._create_route('udf', 'history'),
            get_parms=get_parms,
        )

    def get_global_stats(self) -> dict:
        """
        Get global market stats.

        Returns:
            dict: Response from the server.
        """
        return self._client._send_request(
            method='POST',
            route=self._create_route('global-stats'),
        )