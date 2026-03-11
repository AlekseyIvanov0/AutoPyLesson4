from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_to_basket_btn.click()

    def should_be_confirm_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG), (
            "Message 'product has been added to your basket' is absent"
        )

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG).text
        assert product_name == message_text, 'Message has incorrect product name'

    def should_be_correct_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE_MSG).text
        assert product_price == cart_price
