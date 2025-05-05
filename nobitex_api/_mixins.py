from .routes import (
    Auth,
    Users,
    Orderbook,
    )

class RouteMixin:
    def __init__(self) -> None:
        self.Auth = Auth(self)
        self.Users = Users(self)
        self.Orderbook = Orderbook(self)