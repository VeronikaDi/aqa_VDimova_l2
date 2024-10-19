import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from test_data import TestData


@pytest.fixture(scope="class")
def web_driver():

    driver = webdriver.Chrome(service=Service())

    driver.maximize_window()
    driver.get(TestData().base_url)

    yield driver

    driver.quit()
