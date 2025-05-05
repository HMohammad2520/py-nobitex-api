from .routes import (
    Auth,
    Users,
    )

class RouteMixin:
    def __init__(self) -> None:
        self.Auth = Auth(self)
        self.Users = Users(self)