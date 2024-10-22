from lesson_28.abstract_page import AbstractPage
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(AbstractPage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def sign_in_button(self):
        wait = WebDriverWait(self._driver, 30)
        return wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]"))
        )

    @property
    def registration_button(self):
        wait = WebDriverWait(self._driver, 30)
        return wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[1]"))
        )

    @property
    def name_input(self):
        return self._driver.find_element(By.XPATH, '//*[@id="signupName"]')

    @property
    def last_name_input(self):
        return self._driver.find_element(By.XPATH, '//*[@id="signupLastName"]')

    @property
    def email_input(self):
        return self._driver.find_element(By.XPATH, '//*[@id="signupEmail"]')

    @property
    def password_input(self):
        return self._driver.find_element(By.XPATH, '//*[@id="signupPassword"]')

    @property
    def password_re_input(self):
        return self._driver.find_element(By.XPATH, '//*[@id="signupRepeatPassword"]')

    @property
    def register_button(self):
        return self._driver.find_element(
            By.XPATH, '/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button')

    @property
    def registration_conformation(self):
        return self._driver.find_element(
            By.XPATH, "//div[contains(@class, 'alert alert-success')]//p[text()='Registration complete']")

    def click_sign_in_button(self):
        self.sign_in_button.click()

    def click_registration_button(self):
        self.registration_button.click()

    def enter_name(self, name: str):
        self.name_input.clear()
        self.name_input.send_keys(name)

    def enter_last_name(self, last_name: str):
        self.last_name_input.clear()
        self.last_name_input.send_keys(last_name)

    def enter_email(self, email: str):
        self.email_input.clear()
        self.email_input.send_keys(email)

    def enter_password(self, password: str):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def enter_password_again(self, password: str):
        self.password_re_input.clear()
        self.password_re_input.send_keys(password)

    def click_register_button(self):
        self.register_button.click()
