import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SERVER_URL = os.getenv("TABLEAU_SERVER_URL")
    SITE_ID = os.getenv("TABLEAU_SITE_ID")
    TOKEN_NAME = os.getenv("TABLEAU_TOKEN_NAME")
    TOKEN_VALUE = os.getenv("TABLEAU_TOKEN_VALUE")
    UI_URL = os.getenv("TABLEAU_UI_URL")
    USERNAME = os.getenv("TABLEAU_USERNAME")
    PASSWORD = os.getenv("TABLEAU_PASSWORD")
    BROWSER = os.getenv("BROWSER")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    # Convenience lowercase aliases for use in tests/fixtures
    @property
    def server_url(self) -> str | None:
        return self.SERVER_URL

    @property
    def site_id(self) -> str | None:
        return self.SITE_ID

    @property
    def token_name(self) -> str | None:
        return self.TOKEN_NAME

    @property
    def token_value(self) -> str | None:
        return self.TOKEN_VALUE

    @property
    def ui_url(self) -> str | None:
        return self.UI_URL

    @property
    def username(self) -> str | None:
        return self.USERNAME

    @property
    def password(self) -> str | None:
        return self.PASSWORD

    @property
    def browser(self) -> str | None:
        return self.BROWSER

    @property
    def headless(self) -> bool:
        return self.HEADLESS


config = Config()