from pages.lists_page import ListsPage
import allure
import pytest

class TestLists:
    
    @allure.title("Проверка раскрытия текста 'Сколько это стоит?'")
    def test_how_much(self, driver):
        page = ListsPage(driver)
        page.click_how_much()
        text = page.get_how_much_text()
        assert 'Сутки' in text

    @allure.title("Проверка раскрытия текста 'Хочу несколько самокатов'")
    def test_want_a_few(self, driver):
        page = ListsPage(driver)
        page.click_want_a_few()
        text = page.get_want_a_few_text()
        assert 'Пока что у нас так:' in text
    
    @allure.title("Проверка раскрытия текста 'Как рассчитывается время аренды?'")
    def test_time_rent(self, driver):
        page = ListsPage(driver)
        page.click_time_rent()
        text = page.get_time_rent_text()
        assert 'Допустим, ' in text
    
    @allure.title("Проверка раскрытия текста 'Можно ли заказать самокат на сегодня?'")
    def test_order_today(self, driver):
        page = ListsPage(driver)
        page.click_order_today()
        text = page.get_order_today_text()
        assert 'Только начиная ' in text
    
    @allure.title("Проверка раскрытия текста 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def test_extend_or_return(self, driver):
        page = ListsPage(driver)
        page.click_extend_or_return()
        text = page.get_extend_or_return_text()
        assert 'Пока что нет!' in text
    
    @allure.title("Проверка раскрытия текста 'Вы привозите зарядку вместе с самокатом?'")
    def test_scooter_charger(self, driver):
        page = ListsPage(driver)
        page.click_scooter_charger()
        text = page.get_scooter_charger_text()
        assert 'Самокат приезжает' in text
    
    @allure.title("Проверка раскрытия текста 'Можно ли отменить заказ?'")
    def test_cancel_order(self, driver):
        page = ListsPage(driver)
        page.click_cancel_order()
        text = page.get_cancel_order_text()
        assert 'Штрафа не будет' in text
    
    @allure.title("Проверка раскрытия текста 'Я живу за МКАДом, привезёте?'")
    def test_outside_mkad(self, driver):
        page = ListsPage(driver)
        page.click_outside_mkad()
        text = page.get_outside_mkad_text()
        assert 'Да, обязательно' in text