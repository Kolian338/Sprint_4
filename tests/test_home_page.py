import allure
from selenium import webdriver
from pages.home_page import HomePage
from pages.base_page import BasePage
from helper.data import *


# Класс вопросов
@allure.suite('Тестирование аккордеона')
class TestQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Открывается список вопросов для "Сколько это стоит"')
    def test_accordion_price_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)
        base_page = BasePage(self.driver)

        base_page.open_page('https://qa-scooter.praktikum-services.ru/')

        home_page.scroll_to_accordion_price()
        home_page.click_accordion_price()

        assert home_page.get_accordion_price_description_text() == price_description

    @allure.title('Открывается список вопросов для "Хочу сразу несколько самокатов! Так можно?"')
    def test_accordion_several_scooters_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)

        home_page.click_accordion_several_scooters()

        assert home_page.get_accordion_several_scooters_description_text() == several_scooters_description

    @allure.title('Открывается список вопросов для "Как рассчитывается время аренды?"')
    def test_accordion_rent_calculation_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)

        home_page.click_accordion_rent_calculation()

        assert home_page.get_accordion_rent_calculation_description_text() == rent_calculation_description

    @allure.title('Открывается список вопросов для "Можно ли заказать самокат прямо на сегодня?"')
    def test_accordion_scooter_today_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)

        home_page.click_accordion_scooter_today()

        assert home_page.get_accordion_scooter_today_description_text() == scooter_today_description

    @allure.title('Открывается список вопросов для "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_accordion_extend_or_refund_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)

        home_page.click_accordion_extend_or_refund()

        assert home_page.get_accordion_extend_or_refund_description_text() == extend_or_refund_description

    @allure.title('Открывается список вопросов для "Вы привозите зарядку вместе с самокатом?"')
    def test_accordion_charging_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)

        home_page.click_accordion_charging()

        assert home_page.get_accordion_charging_description_text() == charging_description

    @allure.title('Открывается список вопросов для "Можно ли отменить заказ?"')
    def test_accordion_cancellation_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)

        home_page.click_accordion_cancellation()

        assert home_page.get_accordion_cancellation_description_text() == cancellation_description

    @allure.title('Открывается список вопросов для "Я жизу за МКАДом, привезёте?"')
    def test_accordion_mkad_opening_click_accordion_opened(self):
        home_page = HomePage(self.driver)

        home_page.click_accordion_mkad()

        assert home_page.get_accordion_mkad_description_text() == mkad_description

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
