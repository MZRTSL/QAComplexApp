import pytest
from selenium import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers
from helpers.login_page import LoginHelpers
from helpers.profile_page import ProfileHelpers


class TestLoginPage (BaseTest):

    @pytest.fixture (scope="class")
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    @pytest.fixture (scope="function")
    def logout(self, driver):
        yield
        base_helper=BaseHelpers (driver)
        base_helper.find_by_contains_text (ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click ()

    @pytest.fixture (scope="function")
    def register(self, driver):
        login_helper=LoginHelpers (driver)
        registered_user=login_helper.register_user (username=f"user{self.variety}",
                                                    email=f"mail{self.variety}@mail.com", password=f"Password{self.variety}")
        login_helper.find_by_contains_text (ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click ()
        return registered_user

    def test_invalid_login(self, driver, logout):
        """
        - Open start page
        - Click on Sign In button
        - Verify error message
        """
        login_helper=LoginHelpers (driver)

        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open page")

        # Login as user
        login_helper.login (username="Name1", password="Password1")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info ("Error message match to expected")

    def test_register(self, driver):
        """- Click on Sign Up button
        - Verify register success
        """
        login_helper=LoginHelpers (driver)
        profile_helper=ProfileHelpers (driver)

        # Fill email, login and password fields
        username_value=login_helper.register_user (username=f"user{self.variety}",
                                                   email=f"mail{self.variety}@mail.com", password=f"Password{self.variety}")[0]
        self.log.info ("User was registered")

        # Verify register success
        profile_helper.verify_hello_message (username_value)
        self.log.info ("Registration was success and verified")

    def test_empty_fields_login(self, driver):
        """- Click on Sign In button
        - Verify error message"""

        login_helper=LoginHelpers (driver)

        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open page")

        # Clear password and login fields
        login_helper.login (username="", password="")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.INVALID_LOGIN_MESSAGE_TEXT)
        self.log.info ("Error message match to expected")

    def test_login(self, register, driver, logout):
        """ - Click Sign In button
         - Verify the result"""

        login_helper=LoginHelpers (driver)
        profile_helper=ProfileHelpers (driver)

        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open page")

        username_value, _, password_value=register

        # Clear password and login fields
        login_helper.login (username=username_value, password=password_value)

        # Verify register success
        profile_helper.verify_hello_message (username_value)
        self.log.info ("Registration was success and verified")
