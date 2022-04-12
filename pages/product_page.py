from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def click_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' doesn't find"

    def should_be_added_the_product(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_THE_PRODUCT), "The product didn't add to the basket"

    def basket_price(self):
        print(self.browser.find_element(*ProductPageLocators.BASKET_PRICE))
    
    def concurrence_books_name(self):
        books_name1 = self.browser.find_element(*ProductPageLocators.BOOKS_NAME1).text
        books_name2 = self.browser.find_element(*ProductPageLocators.BOOKS_NAME2).text
        assert books_name1 == books_name2, "Book's names don't coincide"
    
    