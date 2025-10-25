import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    with allure.step('Кликнуть на конструктор'):
        def click_on_constructor(self):
            self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    with allure.step('Проверяем видимость секции Собери бургер'):
        def burger_constructor_visible(self):
            return self.wait_for_element(MainPageLocators.BURGER_CONSTRUCTOR).is_displayed()

    with allure.step('Кликнуть на Ленту заказов'):
        def click_order_feed(self):
            self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    with allure.step('Проверка видимости счетчика выполненных заказов'):
        def order_feed_counter_visible(self):
            return self.wait_for_element(MainPageLocators.READY_ORDERS).is_displayed()

    with allure.step('Кликнуть на ингредиент'):
        def click_on_ingredient(self):
            self.click_to_element(MainPageLocators.FLUORESCENT_BUN)

    with allure.step('Проверка видимости окна Детали ингредиента'):
        def ingredient_details_visible(self):
            return self.element_displayed(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    with allure.step('Закрыть окно Детали ингредиента'):
        def close_ingredient_details(self):
            self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    with allure.step('Получить значение счетчика ингредиентов'):
        def get_ingredient_counter(self):
            return int(self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER))

    with allure.step('Перетащить ингредиент'):
        def drag_and_drop_ingredient(self):
            ingredient = self.wait_for_element(MainPageLocators.FLUORESCENT_BUN)
            top = self.wait_for_element(MainPageLocators.ORDER_PULL_TOP)
            self.drag_and_drop_element(ingredient, top)













