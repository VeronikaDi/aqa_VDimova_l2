import pytest
from main_page import MainPage
from test_data import TestData
from assertpy import assert_that


@pytest.mark.usefixtures("web_driver")
class TestUserRegistration:

    def test_user_registration(self, web_driver):
        web_driver.get(TestData().base_url)
        self.main_page = MainPage(web_driver)

        self.main_page.click_sign_in_button()

        self.main_page.click_registration_button()

        self.main_page.enter_name(TestData().user_name)
        self.main_page.enter_last_name(TestData().user_last_name)
        self.main_page.enter_email(TestData().user_email)
        self.main_page.enter_password(TestData().user_password)
        self.main_page.enter_password_again(TestData().user_password)

        self.main_page.click_register_button()

        success_message = self.main_page.registration_conformation()
        assert_that(success_message).is_equal_to("Registration complete")
