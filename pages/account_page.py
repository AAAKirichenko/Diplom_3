import allure
from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data.data import LOGIN_URL

class AccountPage(BasePage):

    with allure.step('Открыть страницу входа в аккаунт'):
        def open_login_page(self):
            self.transfer_on_page(LOGIN_URL)

    with allure.step('Вход в аккаунт'):
        def login(self, email, password):
            self.open_login_page()
            self.add_text_to_element(AccountPageLocators.EMAIL, email)
            self.add_text_to_element(AccountPageLocators.PASSWORD, password)
            self.js_click(AccountPageLocators.LOGIN_BUTTON)




