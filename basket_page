from selenium.webdriver.common.by import By
from .base_page import BasePage
class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_not_be_products()
        self.should_be_empty_message()

    def should_not_be_products(self):
        assert self.is_not_element_present(
            By.CSS_SELECTOR, ".basket-items"), "Products are in basket, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(
            By.CSS_SELECTOR, "#content_inner>p"), "Empty basket message is not presented"
