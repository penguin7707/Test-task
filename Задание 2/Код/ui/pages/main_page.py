from ui.pages.base_page import BasePage
from ui.pages.cart_page import CartPage
from ui.locators import basic_locators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    url = 'https://www.saucedemo.com/inventory.html'
    locators = basic_locators.MainPageLocators

    def sorted_by_price(self, sign):
        self.click_on_element(basic_locators.MainPageLocators.FILTER)
        if sign == ">":
            self.click_on_element(basic_locators.MainPageLocators.HIGH_TO_LOW)
            price = self.find_elements(basic_locators.MainPageLocators.PRICE1)
            price1 = price[0].text
            price2 = price[1].text
            if float(price1[1:]) > float(price2[1:]):
                return True
        elif sign == "<":
            self.click_on_element(basic_locators.MainPageLocators.LOW_TO_HIGH)
            price = self.find_elements(basic_locators.MainPageLocators.PRICE1)
            price1 = price[0].text
            price2 = price[1].text
            if float(price1[1:]) < float(price2[1:]):
                return True

    def go_to_cart(self):
        self.click_on_element(self.locators.CART)
        return CartPage(self.driver)

    def add_to_cart(self, good):
        locator_to_add = '//button[contains(@id, "add-to-cart-sauce-labs-' + good.lower() + '")]'
        self.click_on_element((By.XPATH, locator_to_add))
