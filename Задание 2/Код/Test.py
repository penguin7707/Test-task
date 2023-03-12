import pytest
from selenium.common import TimeoutException
from base import BaseCase
from ui.pages.base_page import PageNotOpenedExeption
import allure
from selenium.webdriver.common.by import By


class Test_Negative(BaseCase):

    @allure.feature('Negative tests')
    @allure.story('Authorization with invalid login')
    def test_lk1(self):
        self.login_page.login('standard', 'secret_sauce')
        with pytest.raises(PageNotOpenedExeption):
            self.main_page.is_opened()

    @allure.feature('Negative tests')
    @allure.story('Authorization with invalid password')
    def test_lk2(self):
        self.login_page.login('standard_user', 'secret')
        with pytest.raises(PageNotOpenedExeption):
            self.main_page.is_opened()


class Test_positive(BaseCase):
    @allure.feature('Positive tests')
    @allure.story('Sorting goods by price')
    @pytest.mark.parametrize(
        'sign',
        [
            pytest.param(">"),
            pytest.param("<"),
        ],
    )
    def test_sort_by_price(self, sign):
        self.login_page.login('standard_user', 'secret_sauce')
        test_result = self.main_page.sorted_by_price(sign)
        assert test_result == True

    @allure.feature('Positive tests')
    @allure.story('Go to cart')
    def test_go_to_cart(self):
        self.login_page.login('standard_user', 'secret_sauce')
        self.main_page.go_to_cart()
        test_result = self.cart_page.is_opened()
        assert test_result == True

    @allure.feature('Positive tests')
    @allure.story('Back to main page')
    def test_back_to_main_page(self):
        self.login_page.login('standard_user', 'secret_sauce')
        self.main_page.go_to_cart()
        self.cart_page.back_to_main_page()
        test_result = self.main_page.is_opened()
        assert test_result == True

    @allure.feature('Positive tests')
    @allure.story('Adding goods to cart')
    @pytest.mark.parametrize(
        'good',
        [
            pytest.param("backpack"),
            pytest.param("bike-light"),
        ],
    )
    def test_add_to_cart(self, good):
        good_locator = '//button[contains(@id, "remove-sauce-labs-' + good.lower() + '")]/../..//a'
        self.login_page.login('standard_user', 'secret_sauce')
        self.main_page.add_to_cart(good)
        self.main_page.go_to_cart()
        test_result = self.base_page.find_element((By.XPATH, good_locator)).text
        self.cart_page.remove_good(good)
        good = good.replace("-", " ")
        expected_result = "Sauce Labs " + good.title()
        assert test_result == expected_result

    @allure.feature('Positive tests')
    @allure.story('Removing goods from cart')
    @pytest.mark.parametrize(
        'good',
        [
            pytest.param("fleece-jacket"),
            pytest.param("backpack"),
        ],
    )
    def test_remove_from_cart(self, good):
        self.login_page.login('standard_user', 'secret_sauce')
        self.main_page.add_to_cart(good)
        self.main_page.go_to_cart()
        good_locator = self.cart_page.remove_good(good)
        with pytest.raises(TimeoutException):
            self.cart_page.find_element((By.XPATH, good_locator))
