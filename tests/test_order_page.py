import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from data.data import EMAIL, PASSWORD


@allure.title('Тест увеличения счётчика заказа Выполнено за все время')
def test_total_counter_after_new_order_increase(driver):
    order_page = OrderPage(driver)
    main_page = MainPage(driver)
    account_page = AccountPage(driver)

    with allure.step('Вход в аккаунт'):
        account_page.login(EMAIL, PASSWORD)

    with allure.step('Открываем Ленту Заказов'):
        order_page.click_on_feed()

    with allure.step('Получаем общий счётчик заказов'):
        total_orders = order_page.get_total_orders_counter()

    with allure.step('Создаем новый заказ'):
        order_page.click_on_constructor()
        main_page.drag_and_drop_ingredient()
        order_page.click_place_an_order()
        order_page.get_order_id_from_details()
        order_page.click_close_order_details()

    with allure.step('Проверяем, что общий счётчик заказов увеличился'):
        order_page.open_feed_page()
        new_total_orders = order_page.get_total_orders_counter()
        assert new_total_orders > total_orders

@allure.title('Тест увеличения счётчика заказов Выполнено за сегодня')
def test_today_counter_after_new_order_increase(driver):
    order_page = OrderPage(driver)
    main_page = MainPage(driver)
    account_page = AccountPage(driver)

    with allure.step('Выполняем вход в аккаунт'):
        account_page.login(EMAIL, PASSWORD)

    with allure.step('Переходим в Ленту Заказов'):
        order_page.click_on_feed()

    with allure.step('Получаем счётчик заказов за сегодня'):
        today_orders = order_page.get_today_counter()
        order_page.click_on_constructor()

    with allure.step('Создаем новый заказ'):
        order_page.click_on_constructor()
        main_page.drag_and_drop_ingredient()
        order_page.click_place_an_order()
        order_page.get_order_id_from_details()

    with allure.step('Закрываем окно и переходим в Ленту Заказов'):
        order_page.click_close_order_details()
        order_page.click_on_feed()

    with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
        new_today_orders = order_page.get_today_counter()
        assert new_today_orders > today_orders


@allure.title('Тест появления номера заказа в разделе В работе')
def test_number_order_in_progress_after_new_order(driver):
    order_page = OrderPage(driver)
    main_page = MainPage(driver)
    account_page = AccountPage(driver)

    with allure.step('Вход в аккаунт'):
        account_page.login(EMAIL, PASSWORD)

    with allure.step('Создаем новый заказ'):
        order_page.click_on_constructor()
        main_page.drag_and_drop_ingredient()
        order_page.click_place_an_order()

    with allure.step('Получаем идентификатор заказа'):
        order_id = order_page.get_order_id_from_details()

    with allure.step('Закрываем окно и переходим в Ленту Заказов'):
        order_page.click_close_order_details()
        order_page.click_on_feed()

    with allure.step('Проверяем, что номер заказа появился в разделе В работе'):
        assert order_page.order_number_in_progress(order_id)