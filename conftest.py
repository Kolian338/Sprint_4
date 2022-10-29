import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# Фикстура для создания  и закрытия драйвера
@allure.step('Открываем и после теста закрываем браузер FireFox')
@pytest.fixture
def driver_firefox():
    options = webdriver.FirefoxOptions()  # создали объект для опций
    #chrome_options.add_argument('--headless')  # добавили настройку
    options.add_argument('--window-size=1920,1080')  # добавили ещё настройку
    driver = webdriver.Firefox(options=options)  # создали драйвер и передали в него настройки

    yield driver

    driver.quit()
