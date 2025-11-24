from selenium.webdriver.common.by import By

class LocatorsOrder:

    order_top = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    order_down = (By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]")

    name = (By.XPATH, ".//input[@placeholder = '* Имя']")
    surname = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    address = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    subway = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    subway_dropdown_option = (By.XPATH, "//div[@class='select-search__select']//button")
    phone = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    further = (By.XPATH, ".//button[text() = 'Далее']")

    when = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    period = (By.CLASS_NAME, 'Dropdown-placeholder')
    day = (By.XPATH, "//div[text()='сутки']")
    days_3 = (By.XPATH, "//div[text()='трое суток']")
    color_black = (By.ID, 'black')
    color_grey = (By.ID, 'grey')
    comment = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    order_button = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    button_yes = (By.XPATH, ".//button[text()='Да']")
    order_success = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    scooter_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    ya_logo = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    for_whom_scooter = (By.XPATH, ".//div[text() = 'Для кого самокат']")
    want_to_order = (By.XPATH, ".//div[text() = 'Хотите оформить заказ?']")
    placed_order = (By.XPATH, ".//div[text()='Заказ оформлен']")