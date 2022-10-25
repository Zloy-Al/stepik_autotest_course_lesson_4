from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.PARTIAL_LINK_TEXT, "login")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages>.alert:first-child strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages>.alert:last-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:first-child")

