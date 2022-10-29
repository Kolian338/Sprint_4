from selenium.webdriver.common.by import By


class OrderPageLocators:
    url_order = 'https://qa-scooter.praktikum-services.ru/order'
    # Для кого самокат
    name_field = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    surname_field = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    underground_field = [By.CLASS_NAME, 'select-search__input']
    underground_station_first_value = [By.XPATH, ".//button[@value = '1']"]
    phone_field = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, ".//button[text() = 'Далее']"]
    # Про аренду
    datepicker_field = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    datapicker_today_value = [By.CLASS_NAME, 'react-datepicker__day--today']
    rent_field = [By.CLASS_NAME, 'Dropdown-placeholder']
    rent_one_day_value = [By.XPATH, ".//div[@class = 'Dropdown-option' and text()='сутки']"]
    rent_two_days_value = [By.XPATH,".//div[@class = 'Dropdown-option' and text()='двое суток']"]
    scooter_black_color_checkbox = [By.ID, 'black']
    scooter_gray_color_checkbox = [By.ID, 'grey']
    comment_field = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"]
    back_button = [By.XPATH, ".//button[text() = 'Назад']"]
    order_button = [By.XPATH, ".//button[text() = 'Заказать' and contains(@class, 'Button_Middle__1CSJM')]"]
    # Форма подтверждения
    confirm_order_yes_button = [By.XPATH, ".//button[text()= 'Да']"]
    confirm_order_no_button = [By.XPATH, ".//button[text()= 'Нет']"]
    # Заказ оформлен
    order_success_modal_window = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
