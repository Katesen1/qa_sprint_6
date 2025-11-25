from locators.order_locators import LocatorsOrder
from .base_page import BasePage
import allure
import pytest

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликнуть на кнопку 'Заказать' вверху страницы")
    def click_order_top(self):
        self.click_with_scroll(LocatorsOrder.order_top)
    
    @allure.step("Кликнуть на кнопку 'Заказать' внизу страницы")
    def click_order_down(self):
        self.click_with_scroll(LocatorsOrder.order_down)
   
    @allure.step("Заполнить первую форму заказа")
    def first_form(self, name, surname, address, subway, phone):
        self.enter_text(LocatorsOrder.name, name)
        self.enter_text(LocatorsOrder.surname, surname)
        self.enter_text(LocatorsOrder.address, address)
        self.select_subway_station(subway)
        self.enter_text(LocatorsOrder.phone, phone)
        self.click_with_scroll(LocatorsOrder.further)

    @allure.step("Выбрать станцию метро")
    def select_subway_station(self, station):
        subway_element = self.wait_for_element_visible(LocatorsOrder.subway)
        subway_element.click()
        subway_element.send_keys(station)
        self.wait_for_element_clickable(LocatorsOrder.subway_dropdown_option).click()
    
    @allure.step("Выбрать период аренды")
    def select_rental_period(self, period):
        period_locators = {
            'сутки': LocatorsOrder.day,
            'трое суток': LocatorsOrder.days_3
        }
        locator = period_locators[period]
        self.wait_for_element_visible(LocatorsOrder.period).click()
        self.wait_for_element_visible(locator).click()

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color):
        color_locators = {
            'black': LocatorsOrder.color_black,
            'grey': LocatorsOrder.color_grey
        }
        locator = color_locators[color]
        self.wait_for_element_visible(locator).click()
    
    @allure.step("Заполнить вторую форму заказа")
    def second_form(self, date, period, color, comment):
        self.enter_text(LocatorsOrder.when, date)
        self.wait_for_element_visible(LocatorsOrder.order_button).click()
        self.select_rental_period(period)
        self.select_scooter_color(color)
        self.enter_text(LocatorsOrder.comment, comment)
        self.wait_for_element_visible(LocatorsOrder.order_button).click()
        self.wait_for_element_visible(LocatorsOrder.button_yes).click()

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        return self.get_element_text(LocatorsOrder.order_success)
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_with_scroll(LocatorsOrder.scooter_logo)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_ya_logo(self):
        self.click_with_scroll(LocatorsOrder.ya_logo)
        self.switch_to_new_window()