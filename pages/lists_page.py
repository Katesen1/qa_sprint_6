from locators.lists_locators import LocatorsLists
from .base_page import BasePage
import allure
import pytest

class ListsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на вопрос 'Сколько это стоит? И как оплатить?'")
    def click_how_much(self):
        self.click_with_scroll(LocatorsLists.how_much)
    @allure.step("Ответ на 'Сколько это стоит? И как оплатить?'")
    def get_how_much_text(self):
        return self.get_element_text(LocatorsLists.how_much_panel)
    
    @allure.step("Кликнуть на вопрос 'Хочу сразу несколько самокатов! Так можно?'")
    def click_want_a_few(self):
        self.click_with_scroll(LocatorsLists.want_a_few)
    @allure.step("Ответ на 'Хочу сразу несколько самокатов! Так можно?'")
    def get_want_a_few_text(self):
        return self.get_element_text(LocatorsLists.want_a_few_panel)

    @allure.step("Кликнуть на вопрос 'Как рассчитывается время аренды?'")
    def click_time_rent(self):
        self.click_with_scroll(LocatorsLists.time_rent)
    @allure.step("Ответ на 'Как рассчитывается время аренды?'")
    def get_time_rent_text(self):
        return self.get_element_text(LocatorsLists.time_rent_panel)

    @allure.step("Кликнуть на вопрос 'Можно ли заказать самокат на сегодня?'")
    def click_order_today(self):
        self.click_with_scroll(LocatorsLists.order_today)
    @allure.step("Ответ на 'Можно ли заказать самокат на сегодня?'")
    def get_order_today_text(self):
        return self.get_element_text(LocatorsLists.order_today_panel)

    @allure.step("Кликнуть на вопрос 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def click_extend_or_return(self):
        self.click_with_scroll(LocatorsLists.extend_or_return)
    @allure.step("Ответ на 'Можно ли продлить заказ или вернуть самокат раньше?")
    def get_extend_or_return_text(self):
        return self.get_element_text(LocatorsLists.extend_or_return_panel)
    
    @allure.step("Кликнуть на вопрос 'Вы привозите зарядку вместе с самокатом?'")
    def click_scooter_charger(self):
        self.click_with_scroll(LocatorsLists.scooter_charger)
    @allure.step("Ответ на 'Вы привозите зарядку вместе с самокатом?'")
    def get_scooter_charger_text(self):
        return self.get_element_text(LocatorsLists.scooter_charger_panel)

    @allure.step("Кликнуть на вопрос 'Можно ли отменить заказ?'")
    def click_cancel_order(self):
        self.click_with_scroll(LocatorsLists.cancel_order)
    @allure.step("Ответ на 'Можно ли отменить заказ?'")
    def get_cancel_order_text(self):
        return self.get_element_text(LocatorsLists.cancel_order_panel)
    
    @allure.step("Нажать на вопрос 'Я живу за МКАДом, привезёте?'")
    def click_outside_mkad(self):
        self.click_with_scroll(LocatorsLists.outside_mkad)
    @allure.step("Ответ на 'Я живу за МКАДом, привезёте?'")
    def get_outside_mkad_text(self):
        return self.get_element_text(LocatorsLists.outside_mkad_panel)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    