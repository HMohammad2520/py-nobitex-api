# nobitex_api\_mixins.py
from .routes import (
    Auth,
    Depth,
    Market,
    Options,
    Orderbook,
    OTP,
    Security,
    Trades,
    Users,
    Wallets,
)

class RouteMixin:
    def __init__(self) -> None:
        self.Auth = Auth(self)
        self.Depth = Depth(self)
        self.Market = Market(self)
        self.Options = Options(self)
        self.Orderbook = Orderbook(self)
        self.OTP = OTP(self)
        self.Security = Security(self)
        self.Trades = Trades(self)
        self.Users = Users(self)
        self.Wallets = Wallets(self)