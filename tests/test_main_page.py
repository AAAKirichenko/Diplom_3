import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage


class TestMainPage:

    @allure.title('Тест проверки перехода по клику на Конструктор')
    def test_transfer_constructor(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на Конструктор'):
            main_page.click_on_constructor()

        with allure.step('Проверяем, что секция Собери бургер отображается'):
            assert main_page.burger_constructor_visible()

    @allure.title('Тест проверки перехода по клику на Ленту Заказов')
    def test_transfer_order_feed(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на Ленту Заказов'):
            main_page.click_order_feed()

        with allure.step('Проверяем, что счетчик выполненных заказов отображается'):
            assert main_page.order_feed_counter_visible()

    @allure.title('Тест проверки всплывающего окна с деталями, по клику на ингредиент')
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на Конструктор'):
            main_page.click_on_constructor()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_on_ingredient()

        with allure.step('Проверяем, что окно с деталями ингредиента отображается'):
            assert main_page.ingredient_details_visible()

    @allure.title('Тест проверки закрытия всплывающего окна с деталями ингредиента')
    def test_close_details_ingredient(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на Конструктор'):
            main_page.click_on_constructor()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_on_ingredient()

        with allure.step('Закрываем окно с деталями ингредиента'):
            main_page.close_ingredient_details()

        with allure.step('Проверяем, что окно с деталями ингредиента закрыто'):
            assert not main_page.ingredient_details_visible()

    @allure.title('Тест проверка увеличения счетчика ингредиентов')
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на Конструктор'):
            main_page.click_on_constructor()

        with allure.step('Получаем значение счетчика ингредиентов'):
            counter = main_page.get_ingredient_counter()

        with allure.step('Добавляем ингредиент в заказ'):
            main_page.drag_and_drop_ingredient()

        with allure.step('Проверяем, что счетчик увеличился'):
            new_counter = main_page.get_ingredient_counter()
            assert new_counter == counter + 2
