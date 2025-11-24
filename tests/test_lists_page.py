from selenium import webdriver
from pages.lists_page import ListsPage
from locators.lists_locators import LocatorsLists
from selenium.webdriver.support import expected_conditions
import allure

class TestLists:
    
    def test_how_much(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_how_much()
        how_much_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.how_much_panel))
        assert 'Сутки' in how_much_text.text

    def test_want_a_few(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_want_a_few()
        want_a_few_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.want_a_few_panel))
        assert 'Пока что у нас так:' in want_a_few_text.text
    
    def test_time_rent(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_time_rent()
        time_rent_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.time_rent_panel))
        assert 'Допустим, ' in time_rent_text.text
    
    def test_order_today(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_order_today()
        order_today_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.order_today_panel))
        assert 'Только начиная ' in order_today_text.text
    
    def test_extend_or_return(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_extend_or_return()
        extend_or_return_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.extend_or_return_panel))
        assert 'Пока что нет!' in extend_or_return_text.text
    
    def test_scooter_charger(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_scooter_charger()
        scooter_charger_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.scooter_charger_panel))
        assert 'Самокат приезжает' in scooter_charger_text.text
    
    def test_cancel_order(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_cancel_order()
        cancel_order_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.cancel_order_panel))
        assert 'Штрафа не будет' in cancel_order_text.text
    
    def test_outside_mkad(self, driver:webdriver.Firefox):
        page = ListsPage(driver)
        page.click_outside_mkad()
        outside_mkad_text = page.wait.until(expected_conditions.visibility_of_element_located(LocatorsLists.outside_mkad_panel))
        assert 'Да, обязательно' in outside_mkad_text.text