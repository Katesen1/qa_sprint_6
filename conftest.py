from selenium import webdriver
import pytest
import allure
import urls

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()
