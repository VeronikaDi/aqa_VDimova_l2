import pytest
import allure
from assertpy import assert_that
from lesson_30.main_page import MainPage
from lesson_30.test_data import TestData


@allure.feature('Package Tracking')
class TestPackageTracking:

    @allure.step('Open Nova Poshta tracking page')
    def open_tracking_page(self, driver):
        driver.get(TestData().base_url)

    @allure.step('Enter package number')
    def enter_package_number(self, main_page, tracking_number):
        main_page.enter_tracking_number(tracking_number)

    @allure.step('Click search and confirm')
    def search_package(self, main_page):
        main_page.click_search()
        main_page.click_ok()

    @allure.step('Get and verify package status')
    def verify_status(self, main_page):
        actual_status = main_page.get_package_status()
        assert_that(actual_status).is_equal_to("Отримана")

    def test_tracking_package_status(self, web_driver):
        self.main_page = MainPage(web_driver)
        self.open_tracking_page(web_driver)
        self.enter_package_number(self.main_page, TestData().package_number)
        self.search_package(self.main_page)
        self.verify_status(self.main_page)
