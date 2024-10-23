from abc import ABC

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def wait_for_element_to_be_clickable(self, timeout: int = 30) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(self.locator))
