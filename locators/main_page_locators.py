from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    BURGER_CONSTRUCTOR = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    READY_ORDERS = (By.XPATH, "//p[contains(text(),'Готовы:')]")
    FLUORESCENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")
    ORDER_PULL_TOP = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")


