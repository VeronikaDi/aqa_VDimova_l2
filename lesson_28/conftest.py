import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def web_driver():

    driver = webdriver.Chrome(service=Service())

    driver.maximize_window()
    driver.get("https://UserName:Password@qauto2.forstudy.space")

    yield driver

    driver.quit()
