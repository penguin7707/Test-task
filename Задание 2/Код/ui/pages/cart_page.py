from ui.pages.base_page import BasePage
from ui.locators import basic_locators
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    url = 'https://www.saucedemo.com/cart.html'
    locators = basic_locators.CartPageLocators

    def remove_good(self, good):
        locator = '//button[contains(@id, "remove-sauce-labs-' + good.lower() + '")]'
        self.click_on_element((By.XPATH, locator))
        return locator

    def back_to_main_page(self):
        self.click_on_element(basic_locators.CartPageLocators.BACK_TO_MAIN_PAGE)

