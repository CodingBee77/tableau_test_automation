import pytest

from config.config import config
from drivers.driver_factory import DriverFactory
from clients.tableau_client import TableauClient
from clients.workbook_client import WorkbookClient


@pytest.fixture(scope="session")
def app_config():
    """
    Provide the loaded configuration object to tests.
    """
    return config


@pytest.fixture(scope="session")
def tableau_client(app_config):
    """
    Yield a signed-in Tableau Server client for API tests.
    """
    client = TableauClient.from_config(app_config)
    with client.session():
        yield client.server


@pytest.fixture(scope="session")
def workbook_client(app_config):
    """
    Yield a signed-in WorkbookClient for workbook-centric tests.
    """
    client = WorkbookClient.from_config(app_config)
    with client.session():
        yield client


@pytest.fixture
def base_url(app_config):
    """
    Base URL for public Tableau checks.
    """
    return app_config.ui_url or "https://public.tableau.com"


@pytest.fixture
def page(app_config):
    driver = DriverFactory(browser=app_config.browser, headless=app_config.headless)
    page = driver.launch()

    try:
        yield page
    finally:
        driver.close()
