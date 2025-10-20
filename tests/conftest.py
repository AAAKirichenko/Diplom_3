import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from data.data import *


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    with allure.step(f"Запуск теста в браузере: {browser}"):
        allure.dynamic.parameter("Browser", browser)
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    else:
        raise ValueError(f"Неизвестный браузер: {browser}")
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()

