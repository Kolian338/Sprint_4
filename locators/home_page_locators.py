from selenium.webdriver.common.by import By
from helper.data import *


class HomePageLocators:
    url_home = 'https://qa-scooter.praktikum-services.ru/'
    button_order = [By.XPATH, ".//div/div/div/div/div/div/button[text()='Заказать']"]

    accordion_price = [By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']"]
    accordion_several_scooters = [By.XPATH, ".//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    accordion_rent_calculation = [By.XPATH, ".//div[text()='Как рассчитывается время аренды?']"]
    accordion_scooter_today = [By.XPATH, ".//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    accordion_extend_or_refund = [By.XPATH, ".//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    accordion_charging = [By.XPATH, ".//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    accordion_cancellation = [By.XPATH, ".//div[text()='Можно ли отменить заказ?']"]
    accordion_mkad = [By.XPATH, ".//div[text()='Я жизу за МКАДом, привезёте?']"]

    accordion_price_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{price_description}')]"]
    accordion_several_scooters_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{several_scooters_description}')]"]
    accordion_rent_calculation_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{rent_calculation_description}')]"]
    accordion_scooter_today_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{scooter_today_description}')]"]
    accordion_extend_or_refund_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{extend_or_refund_description}')]"]
    accordion_charging_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{charging_description}')]"]
    accordion_cancellation_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{cancellation_description}')]"]
    accordion_mkad_description = [By.XPATH, f".//div[@class = 'accordion']//p[contains(text(), '{mkad_description}')]"]
