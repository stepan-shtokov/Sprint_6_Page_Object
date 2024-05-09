import pytest
import allure
from selenium import webdriver
from helper_data.data import Urls


@allure.step('Open browser / Go to Yandex. Scooter / Close browser')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    driver.get(Urls.BASE_SCOOTER_URL)
    yield driver
    driver.quit()
