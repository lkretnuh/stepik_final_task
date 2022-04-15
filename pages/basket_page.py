from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "Basket isn't empty"

    def should_be_no_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.NO_ITEMS), "Basket isn't empty"