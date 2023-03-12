from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):
    url = 'https://www.saucedemo.com/'

    def login(self, user, password):
        pasword = self.find_element(basic_locators.LoginPageLocators.LOGIN_PASSWORD)
        pasword.clear()
        pasword.send_keys(password)
        login = self.find_element(basic_locators.LoginPageLocators.LOGIN_USERNAME)
        login.clear()
        login.send_keys(user)
        self.click_on_element(basic_locators.LoginPageLocators.LOGIN_BUTTON_LOCATOR)
        return MainPage(self.driver)



