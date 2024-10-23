import pytest
from main_page import MainPage
from test_data import TestData
from assertpy import assert_that


@pytest.mark.usefixtures("web_driver")
class TestUserRegistration:

    def test_user_registration(self, web_driver):
        web_driver.get(TestData.BASE_URL)
        self.main_page = MainPage(web_driver)

        self.main_page.click_sign_in_button()

        self.main_page.click_registration_button()

        self.main_page.enter_name(TestData.USER_NAME)
        self.main_page.enter_last_name(TestData.USER_LAST_NAME)
        self.main_page.enter_email(TestData.USER_EMAIL)
        self.main_page.enter_password(TestData.USER_PASSWORD)
        self.main_page.enter_password_again(TestData.USER_PASSWORD)

        self.main_page.click_register_button()

        success_message = self.main_page.registration_conformation
        assert_that(success_message.text).is_equal_to("Registration complete")
