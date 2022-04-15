from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Current url doesn't contains 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is absent'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'Register form is absent'

    def register_new_user(self, email,password):
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_input.send_keys(email)
        pas1_input = self.browser.find_element(*LoginPageLocators.REG_PAS1)
        pas1_input.send_keys(password)
        pas2_input = self.browser.find_element(*LoginPageLocators.REG_PAS2)
        pas2_input.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button_register.click()