import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    with allure.step('Перейти на страницу'):
        def transfer_on_page(self, url):
            self.driver.get(url)

    with allure.step('Подождать видимости элемента'):
        def wait_for_element(self, locator):
            return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    with allure.step('Кликнуть на элемент'):
        def click_to_element(self, locator):
            element = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()

    with allure.step('Получить текст элемента'):
        def get_text_on_element(self, locator):
            element = self.wait_for_element(locator)
            return element.text

    with allure.step('Ввести текст в поле ввода'):
        def add_text_to_element(self, locator, text):
            self.wait_for_element(locator).send_keys(text)

    with allure.step('Кликнуть на элемент, который перекрыт другим объектом'):
        def js_click(self, locator):
            element = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

    with allure.step('Ждать пока элемент станет видимым'):
        def wait_for_element_visible(self, locator):
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    with allure.step('Кликнуть на элемент, когда он станет кликабельным'):
        def click_when_clickable(self, locator):
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
            self.wait_for_element(locator).click()

    with allure.step('Подождать пока изменится текст элемента'):
        def wait_for_element_change_text(self, locator, initial_text, timeout=60):
            WebDriverWait(self.driver, timeout).until(lambda d: self.get_text_on_element(locator) != initial_text)
            return self.wait_for_element(locator)

    with allure.step('Перетащить элемент'):
        def drag_and_drop_element(self, source, target):
            drag_and_drop(self.driver, source, target)

    with allure.step('Проверка видимости элемента'):
        def element_displayed(self, locator):
            try:
                element = self.wait_for_element(locator)
                return element.is_displayed()
            except TimeoutException:
                return False










