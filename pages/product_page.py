from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_btn.click()

    def go_to_basket(self):
        go_to_basket_btn = self.browser.find_element(*ProductPageLocators.GO_TO_BASKET)
        go_to_basket_btn.click()

    def should_be_product_name_in_basket(self):
        product_name_elem = self.browser.find_element(*ProductPageLocators.PRODUCT)
        product_name = product_name_elem.text
        basket_product_name_elem = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        basket_product_name = basket_product_name_elem.text

        assert product_name == basket_product_name, "This is not your product"

    def should_be_product_price_in_basket(self):
        price_elem = self.browser.find_element(*ProductPageLocators.PRICE)
        price = price_elem.text
        basket_price_elem = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        basket_price = basket_price_elem.text

        assert price == basket_price, "The price in basket doesn't match the price of product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"

    def should_not_be_product_in_basket(self):
        assert not self.is_element_present(*ProductPageLocators.BASKET_CONTAINER), "There are products in the basket"
