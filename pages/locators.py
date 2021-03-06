from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    REG_PAS1 = (By.CSS_SELECTOR, "[name=registration-password1]")
    REG_PAS2 = (By.CSS_SELECTOR, "[name=registration-password2]")
    REG_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")
    REG_CONFIRM = (By.CSS_SELECTOR, "#logout_link")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_THE_PRODUCT =(By.CSS_SELECTOR, ".alertinner")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    BOOKS_NAME1 = (By.CSS_SELECTOR, ".col-sm-6>h1")
    BOOKS_NAME2 = (By.CSS_SELECTOR, ".alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>.btn")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    NO_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")