import tableauserverclient as TSC
from contextlib import contextmanager

from config.config import config


class BaseTableauClient:
    def __init__(self, server_url: str, token_name: str, token_value: str, site_id: str):
        self.auth = TSC.PersonalAccessTokenAuth(token_name, token_value, site_id)
        self.server = TSC.Server(server_url, use_server_version=True)

    @classmethod
    def from_config(cls, cfg=None):
        cfg = cfg or config
        return cls(
            cfg.SERVER_URL,
            cfg.TOKEN_NAME,
            cfg.TOKEN_VALUE,
            cfg.SITE_ID,
        )

    def sign_in(self) -> None:
        self.server.auth.sign_in(self.auth)

    def sign_out(self) -> None:
        self.server.auth.sign_out()

    @contextmanager
    def session(self):
        """
        Sign in for the duration of the context and ensure sign-out.
        Yields the client instance so callers can access `self.server`.
        """
        self.sign_in()
        try:
            yield self
        finally:
            self.sign_out()

