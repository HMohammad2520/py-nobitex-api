from .routes import (
    Auth,
    Depth,
    Market,
    Orderbook,
    Trades,
    Users,
    Wallets,
)

class RouteMixin:
    def __init__(self) -> None:
        self.Auth = Auth(self)
        self.Depth = Depth(self)
        self.Market = Market(self)
        self.Orderbook = Orderbook(self)
        self.Trades = Trades(self)
        self.Users = Users(self)
        self.Wallets = Wallets(self)