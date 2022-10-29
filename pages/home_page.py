import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators

delay = 10


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_order_button(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.button_order))

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_order_button(self):
        self.get_order_button().click()

    # Проксрокллить к кнопке "Заказать"
    @allure.step('Скролл до кнопки "Заказать"')
    def scroll_to_order_button(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_order_button())

    # Проскроллить к вопросам
    def scroll_to_accordion_price(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_accordion_price())

    # Получить аккардеоны
    def get_accordion_price(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_price))

    def get_accordion_several_scooters(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_several_scooters))

    def get_accordion_rent_calculation(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_rent_calculation))

    def get_accordion_scooter_today(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_scooter_today))

    def get_accordion_extend_or_refund(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_extend_or_refund))

    def get_accordion_charging(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_charging))

    def get_accordion_cancellation(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_cancellation))

    def get_accordion_mkad(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(HomePageLocators.accordion_mkad))

    # Нажатие на аккрадеоны
    @allure.step('Нажатие на аккордеон "Сколько это стоит? И как оплатить?" ')
    def click_accordion_price(self):
        self.get_accordion_price().click()

    @allure.step('Нажатие на аккордеон "Хочу сразу несколько самокатов! Так можно?" ')
    def click_accordion_several_scooters(self):
        self.get_accordion_several_scooters().click()

    @allure.step('Нажатие на аккордеон "Как рассчитывается время аренды?" ')
    def click_accordion_rent_calculation(self):
        self.get_accordion_rent_calculation().click()

    @allure.step('Нажатие на аккордеон "Можно ли заказать самокат прямо на сегодня?" ')
    def click_accordion_scooter_today(self):
        self.get_accordion_scooter_today().click()

    @allure.step('Нажатие на аккордеон "Можно ли продлить заказ или вернуть самокат раньше?" ')
    def click_accordion_extend_or_refund(self):
        self.get_accordion_extend_or_refund().click()

    @allure.step('Нажатие на аккордеон "Вы привозите зарядку вместе с самокатом?" ')
    def click_accordion_charging(self):
        self.get_accordion_charging().click()

    @allure.step('Нажатие на аккордеон "Можно ли отменить заказ?" ')
    def click_accordion_cancellation(self):
        self.get_accordion_cancellation().click()

    @allure.step('Нажатие на аккордеон "Я жизу за МКАДом, привезёте?" ')
    def click_accordion_mkad(self):
        self.get_accordion_mkad().click()

    # Получение текста в аккордеоне
    @allure.step('Получение текста в аккордеоне')
    def get_accordion_price_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_price_description).text

    @allure.step('Получение текста в аккордеоне')
    def get_accordion_several_scooters_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_several_scooters_description).text

    @allure.step('Получение текста в аккордеоне')
    def get_accordion_rent_calculation_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_rent_calculation_description).text

    @allure.step('Получение текста в аккордеоне')
    def get_accordion_scooter_today_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_scooter_today_description).text

    @allure.step('Получение текста в аккордеоне')
    def get_accordion_extend_or_refund_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_extend_or_refund_description).text

    @allure.step('Получение текста в аккордеоне')
    def get_accordion_charging_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_charging_description).text

    @allure.step('Получение текста в аккордеоне')
    def get_accordion_cancellation_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_cancellation_description).text

    @allure.step('Получение текста в аккордеоне')
    def get_accordion_mkad_description_text(self):
        return self.driver.find_element(*HomePageLocators.accordion_mkad_description).text



