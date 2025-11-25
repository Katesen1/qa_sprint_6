from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import allure
import pytest

class BasePage:
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step("Клик на элемент")
    def click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Клик на элемент с ожиданием и скроллом")
    def click_with_scroll(self, locator):
        element = self.wait_for_element_visible(locator)
        self.scroll_to_element(element)
        element = self.wait_for_element_clickable(locator)
        self.click_element(element)
    
    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text
    
    @allure.step("Ввести текст в поле")
    def enter_text(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.send_keys(text)
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(EC.url_contains('dzen.ru'))
    
    @allure.step("Проверить URL")
    def check_url_contains(self, text):
        return text in self.driver.current_url