import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time

'''@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])'''
@pytest.mark.add_to_basket
class TestAddToBasketFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.click_add_to_basket()
        #page.solve_quiz_and_get_code()
        button_add_to_basket = ProductPage(browser, browser.current_url)
        button_add_to_basket.should_be_button_add_to_basket()
        added_the_product = ProductPage(browser, browser.current_url)
        added_the_product.should_be_added_the_product()
        concurrence = ProductPage(browser, browser.current_url)
        concurrence.concurrence_books_name()
        basket_price = ProductPage(browser, browser.current_url)
        basket_price.basket_price()
    
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_no_product_in_basket()

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

@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.page = LoginPage(browser, link)
        self.page.open()
        email = str(time.time()) + "@fakemail.org"
        self.page.register_new_user(email,'QWE!@#456rty')
        self.page = BasePage(browser, browser.current_url)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.click_add_to_basket()
        #page.solve_quiz_and_get_code()
        button_add_to_basket = ProductPage(browser, browser.current_url)
        button_add_to_basket.should_be_button_add_to_basket()
        added_the_product = ProductPage(browser, browser.current_url)
        added_the_product.should_be_added_the_product()
        concurrence = ProductPage(browser, browser.current_url)
        concurrence.concurrence_books_name()
        basket_price = ProductPage(browser, browser.current_url)
        basket_price.basket_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()