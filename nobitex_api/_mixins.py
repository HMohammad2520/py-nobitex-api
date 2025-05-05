from .routes import (
    Auth,
    Market,
    Orderbook,
    Trades,
    Users,
)

class RouteMixin:
    def __init__(self) -> None:
        self.Auth = Auth(self)
        self.Market = Market(self)
        self.Orderbook = Orderbook(self)
        self.Trades = Trades(self)
        self.Users = Users(self)