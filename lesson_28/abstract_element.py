from abc import ABC

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class AbstractElement(ABC):

    def __init__(self, driver: WebDriver, locator: tuple[str, str]) -> None:
        self.driver = driver
        self.locator = locator

    def find_element(self) -> WebElement:
        return self.driver.find_element(self.locator)

    def click(self) -> WebElement:
        self.find_element().click()

    def send_keys(self, keys: str) -> WebElement:
        self.find_element().send_keys(keys)

    def get_text(self) -> str:
        return self.find_element().text
