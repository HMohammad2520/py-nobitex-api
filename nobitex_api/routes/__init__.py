# nobitex_api\routes\__init__.py
from .auth import Auth
from .depth import Depth
from .market import Market
from .options import Options
from .orderbook import Orderbook
from .otp import OTP
from .security import Security
from .trades import Trades
from .users import Users
from .wallets import Wallets


__all__ = [
    'Auth',
    'Depth',
    'Market',
    'Options',
    'Orderbook',
    'OTP',
    'Security',
    'Trades',
    'Users',
    'Wallets',
]