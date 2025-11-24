from locators.lists_locators import LocatorsLists
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import allure

class ListsPage:

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _click_accordion(self, locator):
        elem = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        elem = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", elem)

    def click_how_much(self):
        self._click_accordion(LocatorsLists.how_much)
    
    def click_want_a_few(self):
        self._click_accordion(LocatorsLists.want_a_few)
    
    def click_time_rent(self):
        self._click_accordion(LocatorsLists.time_rent)

    def click_order_today(self):
        self._click_accordion(LocatorsLists.order_today)

    def click_extend_or_return(self):
        self._click_accordion(LocatorsLists.extend_or_return)
    
    def click_scooter_charger(self):
        self._click_accordion(LocatorsLists.scooter_charger)

    def click_cancel_order(self):
        self._click_accordion(LocatorsLists.cancel_order)
    
    def click_outside_mkad(self):
        self._click_accordion(LocatorsLists.outside_mkad)
