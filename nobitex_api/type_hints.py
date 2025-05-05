from typing import Literal, TypeAlias

RequestMethod: TypeAlias = Literal['GET', 'POST', 'PUT', 'DELETE']
NobitexBool: TypeAlias = Literal['yes', 'no']
NobitexCaptcha: TypeAlias = Literal['api',]

__all__ = [
    'RequestMethod',
    'NobitexBool',
    'NobitexCaptcha',
]