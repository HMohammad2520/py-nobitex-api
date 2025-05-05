from .routes import (
    Auth,
    Orderbook,
    Trades,
    Users,
    )

class RouteMixin:
    def __init__(self) -> None:
        self.Auth = Auth(self)
        self.Orderbook = Orderbook(self)
        self.Trades = Trades(self)
        self.Users = Users(self)