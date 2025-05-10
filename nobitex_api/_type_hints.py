# nobitex_api\_type_hints.py
from typing import Literal, TypeAlias

RequestMethod: TypeAlias = Literal['GET', 'POST', 'PUT', 'DELETE']
NobitexBool: TypeAlias = Literal['yes', 'no']
NobitexCaptcha: TypeAlias = Literal['api', None]

CurrencyAgainstMode: TypeAlias = Literal['irt', 'usdt']

__all__ = [
    'RequestMethod',
    'NobitexBool',
    'NobitexCaptcha',
    'CurrencyAgainstMode',
]