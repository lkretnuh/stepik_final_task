from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_THE_PRODUCT =(By.CSS_SELECTOR, ".alertinner")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    BOOKS_NAME1 = (By.CSS_SELECTOR, ".col-sm-6>h1")
    BOOKS_NAME2 = (By.CSS_SELECTOR, ".alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
