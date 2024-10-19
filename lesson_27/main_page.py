from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from lesson_27.abstract_page import AbstractPage
from abstract_page import WebDriver


class MainPage(AbstractPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def tracking_input(self):
        return self._driver.find_element(By.XPATH, '//input[@placeholder="Номер посилки"]')

    @property
    def search_button(self):
        wait = WebDriverWait(self._driver, 30)
        return wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="np-number-input-desktop-btn-search-en"]'))
        )

    @property
    def ok_button(self):
        wait = WebDriverWait(self._driver, 30)
        return wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="chat"]/div[2]/button/span'))
        )

    def enter_tracking_number(self, tracking_number: str):
        self.tracking_input.clear()
        self.tracking_input.send_keys(tracking_number)

    def click_search(self):
        self.search_button.click()

    def click_ok(self):
        self.ok_button.click()

    def get_package_status(self):
        wait = WebDriverWait(self._driver, 30)
        status_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="header__status-text"]'))
        )
        return status_element.text
