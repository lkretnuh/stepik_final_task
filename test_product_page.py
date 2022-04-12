from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
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
    basket_price.basket_price()