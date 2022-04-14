import pytest
from .pages.product_page import ProductPage
#import pytest
'''
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])'''

'''def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    button_add_to_basket = ProductPage(browser, browser.current_url)
    button_add_to_basket.should_be_button_add_to_basket()
    added_the_product = ProductPage(browser, browser.current_url)
    added_the_product.should_be_added_the_product()
    concurrence = ProductPage(browser, browser.current_url)
    concurrence.concurrence_books_name()
    basket_price = ProductPage(browser, browser.current_url)
    basket_price.basket_price()'''
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.click_add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.click_add_to_basket()
    page.element_disappeared()