import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

delay = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки {url}')
    def wait_for_load_page(self, url):
        WebDriverWait(self.driver, delay).until(EC.url_to_be(url))

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Открываем страницу {page}')
    def open_page(self, page):
        self.driver.get(page)

    def get_button_order_header(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(BasePageLocators.button_order_header))

    @allure.step('Нажатие на кнопку "Заказать" в шапке')
    def click_button_order_header(self):
        self.get_button_order_header().click()

    def get_logo_scooter(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(BasePageLocators.logo_scooter))

    @allure.step('Нажатие на логотип Самокат')
    def click_logo_scooter(self):
        self.get_logo_scooter().click()

    @allure.step('Нажатие на логотип Yandex')
    def get_logo_yandex(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(BasePageLocators.logo_yandex))

    def click_logo_yandex(self):
        self.get_logo_yandex().click()
