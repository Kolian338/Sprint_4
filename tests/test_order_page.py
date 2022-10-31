import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.order_page import OrderPageLocators
from pages.base_page import BasePageLocators
from pages.home_page import HomePageLocators
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.order_page import OrderPage


# Класс заказа
@allure.suite('Тестирование заказа самоката')
class TestOrderPage:

    driver = None

    @allure.title('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа через кнопку вверху.')
    @allure.description('Оформляется заказ самоката на один день через кнопку заказа в шапке')
    def test_order_from_header_button_success_message(self, driver_firefox):
        self.driver = driver_firefox

        base_page = BasePage(self.driver)
        order_page = OrderPage(self.driver)

        base_page.open_page('https://qa-scooter.praktikum-services.ru/')
        base_page.click_button_order_header()

        order_page.create_order_one_day(name='Николай', surname='Тест', address='Ленина 1', phone='89139131313', comment='Тестовый коммент')

        assert order_page.get_order_success_modal_window().is_displayed()

    @allure.title('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа через кнопку внизу.')
    @allure.description('Оформляется заказ самоката на два дня через кнопку заказа внизу')
    def test_order_from_down_button_success_message(self, driver_firefox):
        self.driver = driver_firefox

        home_page = HomePage(self.driver)
        order_page = OrderPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.open_page('https://qa-scooter.praktikum-services.ru/')
        home_page.scroll_to_order_button()
        home_page.click_order_button()

        order_page.create_order_two_days(name='Николай', surname='Тест', address='Ленина 1', phone='89139131313', comment='Тестовый коммент')

        assert order_page.get_order_success_modal_window().is_displayed()

    @allure.title('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')
    def test_go_to_main_page_click_scooter_logo_from_order_page_goes_to_main_page(self, driver_firefox):
        self.driver = driver_firefox

        home_page = HomePage(self.driver)
        base_page = BasePage(self.driver)

        base_page.open_page('https://qa-scooter.praktikum-services.ru/')
        home_page.scroll_to_order_button()
        home_page.click_order_button()

        base_page.click_logo_scooter()

        assert self.driver.current_url == HomePageLocators.url_home
    @allure.title('Если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса')
    def test_go_to_yandex_page_click_yandex_logo_from_order_page_goes_to_yandex_page_new_tab(self, driver_firefox):
        self.driver = driver_firefox

        home_page = HomePage(self.driver)
        base_page = BasePage(self.driver)

        base_page.open_page('https://qa-scooter.praktikum-services.ru/')
        home_page.scroll_to_order_button()
        home_page.click_order_button()

        base_page.click_logo_yandex()
        base_page.switch_to_new_tab()
        base_page.wait_for_load_page(BasePageLocators.url_dzen)

        assert self.driver.current_url == BasePageLocators.url_dzen
