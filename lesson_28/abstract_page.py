from abc import ABC
from selenium.webdriver.ie.webdriver import WebDriver


class AbstractPage(ABC):
    _driver: WebDriver

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
