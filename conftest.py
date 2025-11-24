from selenium import webdriver
import pytest
import allure

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://qa-scooter.praktikum-services.ru')
    yield driver
    driver.quit()
