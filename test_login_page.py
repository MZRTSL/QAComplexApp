"""Store tests related to star page"""
from time import sleep

import pytest
from selenium import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers
from helpers.login_page import LoginHelpers
from helpers.profile_page import ProfileHelpers


class TestLoginPage1 (BaseTest):

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    @pytest.fixture (scope="function")
    def logout(self, driver):
        yield
        base_helper=BaseHelpers (driver)
        base_helper.find_by_contains_text (ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click ()
        sleep (1)

    @pytest.fixture (scope="function")
    def register(self, driver):
        login_helper=LoginHelpers (driver)
        registered_user=login_helper.register_user (username=f"user{self.variety}",
                                                    email=f"mail{self.variety}@mail.com",
                                                    password=f"PwWddd{self.variety}")
        login_helper.find_by_contains_text (ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click ()
        sleep (1)
        return registered_user

    def test_empty_fields_login(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear password and login fields;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # login as user
        login_helper.login (username="", password="")
        self.log.info ("Clicked on 'Sign In'")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT)
        self.log.info ("Error message match to expected")

    def test_invalid_fields_login(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear password and login fields;
        - Fill fields with invalid values;
         - Click on Sign In button;
         - Verify error message;
        """

        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # login as user
        login_helper.login (username="invalid name", password="P098")
        self.log.info ("Clicked on 'Sign In'")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT)
        self.log.info ("Error message match to expected")

    def test_empty_fields_in_registration_form(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear username, e-mail, password fields;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear required fields
        login_helper.register_user (username="", email="", password="")
        self.log.info ("Clear required fields and clicked on 'Sign In' button")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT)
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT)
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT)
        self.log.info ("Error message match to expected")

    def test_valid_fields_login(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear username, e-mail, password fields;
        - Pick a valid username;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear required fields and Add valid value in username field
        login_helper.register_user (username="test", email="", password="")
        self.log.info ("Username field are filled with valid value and clear other")

        # Verify error message

        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_USER_ALREADY_TAKEN_TEXT)
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT)
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT)
        self.log.info ('Error message match to expected')

    def test_valid_email_only(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear username, e-mail, password fields;
        - Pick a valid email ;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear required fields
        login_helper.register_user (username="", email="test@test.com", password="")
        self.log.info ("Field valid email only and click button")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT)
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MASSAGE_EMAIL_ALREADY_USED_TEXT)
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT)
        self.log.info ('Error message match to expected')

    def test_invalid_password_only(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear username, e-mail, password fields;
        - Pick a invalid password (more that 50 characters);
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear required fields

        login_helper.register_user (username="", email="", password="test1234test1234test1234test1234test1234")
        self.log.info ("Field invalid password only and click button")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT)
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT)
        self.log.info ('Error message match to expected')

    def test_cyrillic_values_in_registration_form(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear username, e-mail, password fields;
        - Add a Cyrillic user name, e-mail, password;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear required fields

        login_helper.register_user (username="Александр", email="тест@тест.юа", password="тест123тест123тест")
        self.log.info ("Field are filled with cyrillic text and click button")

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.ERROR_MESSAGE_CYRILLIC_USER_NAME_TEXT)
        self.log.info ('Error message match to expected')

    def test_cyrillic_values_in_login_form(self, driver):
        login_helper=LoginHelpers (driver)
        """
        - Open start page;
        - Clear username, password fields for Sing In form;
        - Add a Cyrillic user name, password for Sing In form;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear and add username and password fields
        login_helper.login (username="неправильное имя", password="парольпароль")
        self.log.info ("Clicked on 'Sign In'")
        sleep (2)

        # Verify error message
        login_helper.verify_error_message (text=LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT)
        self.log.info ("Error message match to expected")

    def test_register(self, driver, logout):
        """
        - Open start page
        - Fill email, login and password fields
        - Click on Sign Up button
        - Verify register success
        """
        login_helper=LoginHelpers (driver)
        profile_helper=ProfileHelpers (driver)

        # Fill email, login and password fields
        username_value=login_helper.register_user (username=f"user{self.variety}", email=f"mail{self.variety}@mail.com", password=f"PwWWddd{self.variety}")[0]
        self.log.info ("User was registered")

        # Verify register success
        profile_helper.verify_hello_message (username_value)
        self.log.info ("Registration was success and verified")

    def test_login(self, register, driver, logout):
        """- Click Sign In button
        - Verify the result
        """
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
