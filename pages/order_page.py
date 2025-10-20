from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data.data import FEED_URL


class OrderPage(BasePage):

    def click_on_feed(self):
        self.wait_for_element_visible(OrderPageLocators.BURGER_TITLE)
        self.js_click(OrderPageLocators.ORDER_FEED_BUTTON)

    def get_total_orders_counter(self):
        return int(self.get_text_on_element(OrderPageLocators.TOTAL_COUNTER))

    def click_place_an_order(self):
        self.click_to_element(OrderPageLocators.PLACE_AN_ORDER)

    def get_order_id_from_details(self):
        self.wait_for_element_change_text(OrderPageLocators.ORDER_ID, "9999")
        return self.get_text_on_element(OrderPageLocators.ORDER_ID)

    def click_close_order_details(self):
        self.click_when_clickable(OrderPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    def open_feed_page(self):
        self.transfer_on_page(FEED_URL)
        self.wait_for_element_visible(OrderPageLocators.FEED_TITLE)

    def click_on_constructor(self):
        self.click_to_element(OrderPageLocators.CONSTRUCTOR_BUTTON)

    def get_today_counter(self):
        element = self.wait_for_element(OrderPageLocators.TODAY_COUNTER)
        return int(element.text.strip())

    def order_number_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        formatted_locator = self.format_locator(OrderPageLocators.ORDER_IN_PROGRES, formatted_id)
        return self.wait_for_element(formatted_locator)

    def format_locator(self, locator, value):
        method, template = locator
        formatted_string = template.format(value)
        return (method, formatted_string)




















