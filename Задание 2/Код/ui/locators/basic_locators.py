from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//input[contains(@id, "login-button")]')
    LOGIN_USERNAME = (By.XPATH, '//input[contains(@id, "user-name")]')
    LOGIN_PASSWORD = (By.XPATH, '//input[contains(@id, "password")]')


class MainPageLocators:
    FILTER = (By.XPATH, '//select[contains(@class, "product_sort_container")]')
    HIGH_TO_LOW = (By.XPATH, '//option[contains(@value, "hilo")]')
    LOW_TO_HIGH = (By.XPATH, '//option[contains(@value, "lohi")]')
    PRICE1 = (By.XPATH, '//div[contains(@class, "inventory_item_price")]')
    CART = (By.XPATH, '//a[contains(@class, "cart_link")]')
    GOOD = (By.XPATH, '//div[contains(@class, "inventory_item_name")]')


class CartPageLocators:
    BACK_TO_MAIN_PAGE = (By.XPATH, '//button[contains(@id, "continue-shopping")]')
