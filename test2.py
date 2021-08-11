"""Store tests related to start page"""

import pytest
from selenium import webdriver

from conftest import BaseTest


class TestLoginPage (BaseTest):

    @pytest.fixture (scope="class")
    def driver(self):
        driver = webdriver.Chrome (executable_path="/Users/deniskondratuk/PycharmProjects/QaComplexApp/drivers/chromedriver")
        yield driver
        driver.close ()

    def test_empty_fields_login(self, driver):
        """
        - Open start page
        - Clear password and login fields
        - Click on Sign In button
        - Verify error message
        """
        # Open start page
        driver.get ("https://qa-complex-app-for-testing.herokuapp.com")
        self.log.info ("Open page")

        # Clear required fields
        username = driver.find_element_by_xpath (".//input[@placeholder='Username']")
        username.clear ()
        password = driver.find_element_by_xpath (".//input[@placeholder='Password']")
        password.clear ()
        self.log.info ("Fields were cleared")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath (".//button[contains(text(), 'Sign In')]")
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")

        # Verify error message
        error_message = driver.find_element_by_xpath (".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info ("Error message match to expected")
