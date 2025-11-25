from pages.order_page import OrderPage
import pytest
import allure
import urls

class TestOrder:
     @allure.title("Полный флоу заказа через верхнюю кнопку")
     @pytest.mark.parametrize('name,surname,address,subway,phone,date,period,color,comment', [
        (
            'Павел', 'Соколов', 'ул. Марата, д.86', 'Нижегородская', '+79214567832',
            '28.11.2025', 'сутки', 'black', 'вход со двора'
        )
    ])
     def test_complete_order_top_button(self, driver, name, surname, address, subway, phone, date, period, color, comment):
        page = OrderPage(driver)
        page.click_order_top()
        page.first_form(name, surname, address, subway, phone)
        page.second_form(date, period, color, comment)
        assert 'Заказ оформлен' in page.get_success_message()

     @allure.title("Полный флоу заказа через нижнюю кнопку")    
     @pytest.mark.parametrize('name,surname,address,subway,phone,date,period,color,comment', [
        (
            'Алена', 'Логинова', 'ал.Поликарпова, д.2', 'Бульвар Рокоссовского', '+79113450967',
            '29.11.2025', 'трое суток', 'grey', 'позвонить за час'
        )
    ])
     def test_complete_order_button_down(self, driver, name, surname, address, subway, phone, date, period, color, comment):
        page = OrderPage(driver)
        page.click_order_down()
        page.first_form(name, surname, address, subway, phone)
        page.second_form(date, period, color, comment)
        assert 'Заказ оформлен' in page.get_success_message()

     @allure.title("Проверка перехода на главную через логотип Самоката")
     def test_scooter_logo(self, driver):
        page = OrderPage(driver)
        driver.get(urls.BASE_URL+urls.ORDER_URL)
        page.click_scooter_logo()
        assert driver.current_url == urls.BASE_URL
     
     @allure.title("Проверка перехода на Дзен через логотип Яндекса") 
     def test_ya_logo(self, driver):
        page = OrderPage(driver)
        page.click_ya_logo()
        assert page.check_url_contains('dzen.ru')

