from drivers.driver_factory import DriverFactory
from pages.login_page import LoginPage


def test_user_can_login(config):

    driver = DriverFactory()
    page = driver.launch()

    login_page = LoginPage(page)

    login_page.navigate(config.ui_url)

    login_page.login(config.username, config.password)

    assert "home" in page.url

    driver.close()
