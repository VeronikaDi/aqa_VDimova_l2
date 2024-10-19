import pytest
from assertpy import assert_that
from main_page import MainPage
from test_data import TestData


class TestPackageTracking:
    def test_tracking_package_status(self, web_driver):
        web_driver.get(TestData().base_url)

        self.main_page = MainPage(web_driver)
        self.main_page.enter_tracking_number(TestData().package_number)

        self.main_page.click_search()
        self.main_page.click_ok()

        self.actual_status = self.main_page.get_package_status()

        assert_that(self.actual_status).is_equal_to("Отримана")
