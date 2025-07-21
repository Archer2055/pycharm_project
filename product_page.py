from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage
from .locators import ProductPageLocators
from .basket_page import BasketPage
class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_button.click()

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

    def should_be_product_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in message, f"Product name '{product_name}' not in success message"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price in basket_total, f"Product price '{product_price}' not in basket total"

    def should_be_basket_total_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price in message, f"Expected '{product_price}' in message, but got '{message}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"
    def should_be_empty(self):
        basket_page = BasketPage(self.browser, self.browser.current_url)
        basket_page.should_be_empty()
