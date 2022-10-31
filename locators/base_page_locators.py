from selenium.webdriver.common.by import By


class BasePageLocators:
    url_dzen = "https://dzen.ru/?yredirect=true"
    button_order_header = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text() = 'Заказать']"]
    logo_scooter = [By.XPATH, ".//img[@alt='Scooter']"]
    logo_yandex = [By.XPATH, ".//img[@alt='Yandex']"]
