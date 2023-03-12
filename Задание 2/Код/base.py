import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.cart_page import CartPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.main_page: MainPage = (request.getfixturevalue('main_page'))
        self.cart_page: CartPage = (request.getfixturevalue('cart_page'))
        self.login_page = LoginPage(driver)


