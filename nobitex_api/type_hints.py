from typing import Literal, TypeAlias

RequestMethod: TypeAlias = Literal['GET', 'POST', 'PUT', 'DELETE']
NobitexBool: TypeAlias = Literal['yes', 'no']
NobitexCaptcha: TypeAlias = Literal['api', None]

CurrencyMode: TypeAlias = Literal['irt', 'usdt', 'symbol']

__all__ = [
    'RequestMethod',
    'NobitexBool',
    'NobitexCaptcha',
    'CurrencyMode',
]