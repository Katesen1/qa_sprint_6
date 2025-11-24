from locators.order_locators import LocatorsOrder
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import pytest
import allure

class OrderPage:

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_order_top(self):
        self.driver.find_element(*LocatorsOrder.order_top).click()
    
    def click_order_down(self):
        elem = self.wait.until(expected_conditions.visibility_of_element_located(LocatorsOrder.order_down))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
        self.wait.until(expected_conditions.element_to_be_clickable(LocatorsOrder.order_down))
        self.driver.execute_script("arguments[0].click();", elem)
   
    def first_form(self, name, surname, address, subway, phone):
        self.wait.until(expected_conditions.visibility_of_element_located(LocatorsOrder.name)).send_keys(name)
        self.driver.find_element(*LocatorsOrder.surname).send_keys(surname)
        self.driver.find_element(*LocatorsOrder.address).send_keys(address)
        self.driver.find_element(*LocatorsOrder.subway).click()
        self.driver.find_element(*LocatorsOrder.subway).send_keys(subway)
        self.wait.until(expected_conditions.element_to_be_clickable(LocatorsOrder.subway_dropdown_option)).click()
        self.driver.find_element(*LocatorsOrder.phone).send_keys(phone)
        self.driver.find_element(*LocatorsOrder.further).click()

    def select_rental_period(self, period):
        period_locators = {
            'сутки': LocatorsOrder.day,
            'трое суток': LocatorsOrder.days_3
        }
        locator = period_locators[period]
        self.driver.find_element(*LocatorsOrder.period).click()
        self.driver.find_element(*locator).click()

    def select_scooter_color(self, color):
        color_locators = {
            'black': LocatorsOrder.color_black,
            'grey': LocatorsOrder.color_grey
        }
        locator = color_locators[color]
        self.driver.find_element(*locator).click()
    
    def second_form(self, date, period, color, comment):
        self.wait.until(expected_conditions.visibility_of_element_located(LocatorsOrder.when)).send_keys(date)
        self.driver.find_element(*LocatorsOrder.order_button).click()
        self.select_rental_period(period)
        self.select_scooter_color(color)
        self.driver.find_element(*LocatorsOrder.comment).send_keys(comment)
        self.driver.find_element(*LocatorsOrder.order_button).click()
        self.wait.until(expected_conditions.visibility_of_element_located(LocatorsOrder.button_yes)).click()

    def get_success_message(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(LocatorsOrder.order_success)).text
    
    def click_scooter_logo(self):
        self.driver.find_element(*LocatorsOrder.scooter_logo).click()
    
    def click_ya_logo(self):
        self.driver.find_element(*LocatorsOrder.ya_logo).click()
        self.wait.until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(expected_conditions.url_contains('dzen.ru'))