import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators

delay = 10


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
    # Получить элементы
    # Форма Для кого самокат

    def get_name_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.name_field))

    def get_surname_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.surname_field))

    def get_address_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.address_field))

    def get_underground_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.underground_field))

    def get_underground_station_first_value(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.underground_station_first_value))

    def get_phone_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.phone_field))

    def get_next_button(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.next_button))

    # Форма Про аренду
    def get_datepicker_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.datepicker_field))

    def get_datapicker_today_value(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.datapicker_today_value))

    def get_rent_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.rent_field))

    def get_rent_one_day_value(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.rent_one_day_value))

    def get_rent_two_days_value(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.rent_two_days_value))

    def get_scooter_black_color_checkbox(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.scooter_black_color_checkbox))

    def get_scooter_gray_color_checkbox(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.scooter_gray_color_checkbox))

    def get_comment_field(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.comment_field))

    def get_order_button(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.order_button))

    # Форма подтверждения
    def get_confirm_order_yes_button(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.confirm_order_yes_button))

    # Заказ оформлен
    @allure.step('Появилось окно об успешном заказе')
    def get_order_success_modal_window(self):
        return WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable(OrderPageLocators.order_success_modal_window))


    # Действия с элементами
    # Форма Для кого самокат
    def set_name_field(self, name):
        self.get_name_field().send_keys(name)

    def set_surname_field(self, surname):
        self.get_surname_field().send_keys(surname)

    def set_address_field(self, address):
        self.get_address_field().send_keys(address)

    def click_underground_field(self):
        self.get_underground_field().click()

    def click_underground_station_first_value(self):
        self.get_underground_station_first_value().click()

    def set_phone_field(self, phone):
        self.get_phone_field().send_keys(phone)

    def click_next_button(self):
        self.get_next_button().click()

    # Форма Про аренду
    def click_datepicker_field(self):
        self.get_datepicker_field().click()

    def click_datapicker_today_value(self):
        self.get_datapicker_today_value().click()

    def click_rent_field(self):
        self.get_rent_field().click()

    def click_rent_one_day_value(self):
        self.get_rent_one_day_value().click()

    def click_rent_two_days_value(self):
        self.get_rent_two_days_value().click()

    def click_scooter_black_color_checkbox(self):
        self.get_scooter_black_color_checkbox().click()

    def set_comment_field(self, comment):
        self.get_comment_field().send_keys(comment)

    def click_order_button(self):
        self.get_order_button().click()

    # Форма подтверждения
    def click_confirm_order_yes_button(self):
        self.get_confirm_order_yes_button().click()

    # Общие действия
    @allure.step('Оформление самоката на один день')
    def create_order_one_day(self, name, surname, address, phone, comment):
        self.set_name_field(name)
        self.set_surname_field(surname)
        self.set_address_field(address)
        self.click_underground_field()
        self.click_underground_station_first_value()
        self.set_phone_field(phone)
        self.click_next_button()

        self.click_datepicker_field()
        self.click_datapicker_today_value()
        self.click_rent_field()
        self.click_rent_one_day_value()
        self.click_scooter_black_color_checkbox()
        self.set_comment_field(comment)
        self.click_order_button()
        self.click_confirm_order_yes_button()

    @allure.step('Оформление самоката на два дня')
    def create_order_two_days(self, name, surname, address, phone, comment):
        self.set_name_field(name)
        self.set_surname_field(surname)
        self.set_address_field(address)
        self.click_underground_field()
        self.click_underground_station_first_value()
        self.set_phone_field(phone)
        self.click_next_button()

        self.click_datepicker_field()
        self.click_datapicker_today_value()
        self.click_rent_field()
        self.click_rent_two_days_value()
        self.click_scooter_black_color_checkbox()
        self.set_comment_field(comment)
        self.click_order_button()
        self.click_confirm_order_yes_button()

