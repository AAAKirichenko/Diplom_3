from selenium.webdriver.common.by import By

class AccountPageLocators:
    EMAIL = (By.XPATH, "//input[@name='name']")
    PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button_button__33qZ0')
