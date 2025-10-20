from selenium.webdriver.common.by import By

class OrderPageLocators:
    PLACE_AN_ORDER = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    TOTAL_COUNTER = (By.XPATH, "//div[@class='undefined mb-15']//p[contains(@class, 'OrderFeed_number__2MbrQ') and normalize-space(text())]")
    TODAY_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    CLOSE_ORDER_DETAILS_BUTTON = (By.XPATH, "//button[@type='button']//*[name()='svg']")
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")
    ORDER_IN_PROGRES = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]")
    FEED_TITLE = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")
    BURGER_TITLE = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")



