"""Store tests related to star page"""
# from distutils.log import Log
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers
from helpers.login_page import LoginHelpers


class TestLoginPage1 (BaseTest):

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    @pytest.fixture (scope="function")
    def register(self, driver):
        base_helper=BaseHelpers (driver)
        registered_user=self.register_user
        base_helper.find_by_contains_text (ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click ()
        sleep (1)
        return registered_user

    @pytest.fixture (scope="function")
    def logout(self, driver):
        yield
        base_helper=BaseHelpers (driver)
        base_helper.find_by_contains_text (ProfilePage.SIGN_OUT_BUTTON_TEXT, "button").click ()
        sleep (1)

    def test_register(self, driver, logout):
        """
        -  Open page
        - Fill login, email, password
        - Click on Sign Up Button
        - Verify success
        """
        login_helper=LoginHelpers (driver)
        username_value=login_helper.test_registered_user (username=f"user{self.variety}",
                                                          email=f"mail{self.variety}@gmail.com",
                                                          password=f"Paw{self.variety}")

        self.log.info ("User was registered")

        # Verified registered success
        hello_message=driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_XPATH)
        assert username_value.lower () in hello_message
        assert hello_message.text == ProfilePage.HELLO_MESSAGE_TEXT.format (lower_username=username_value.lower)
        assert driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username_value.lower ()
        self.log.info ("Registration was success and verified")

    def register_user(self, register, driver, logout):
        base_helper=BaseHelpers (driver)
        """
        -Open start page
        - Fill e-mail and password
        - Click Sign In
        - Verify result
        """

        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        username_value, _, password_value=register

        # Clear and fill username, password Sing In form;
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH,
                                       value=username_value)
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH,
                                       value=password_value)
        sleep (1)

        # Click on Sign In button
        sign_in_button=base_helper.find_by_contains_text (text=LoginPageConstants.SIGN_IN_BUTTON_TEXT,
                                                          element_tag="button")
        sign_in_button.click ()
        self.log.info ("Click on Sign In")
        sleep (1)

        # Verify register success
        hello_message=base_helper.find_by_contains_text (ProfilePage.HELLO_MESSAGE_TEXT)
        assert username_value.lower () in hello_message.text
        assert driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username_value.lower ()
        self.log.info ("Registration was success and verified")

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

        # Verify error message
        error_message=login_helper.find_by_contains_text (LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT)
        assert error_message.text == LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT
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

        # Verify error message
        error_message=login_helper.find_by_contains_text (LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT)
        assert error_message.text == LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT
        self.log.info ("Error message match to expected")
        sleep (1)

    def test_empty_fields_in_registration_form(self, driver):
        base_helper=BaseHelpers (driver)
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
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        self.log.info ("Clear required fields")

        # Click on Sign UP button
        sign_up_button=base_helper.find_by_contains_text (text=LoginPageConstants.SIGN_UP_BUTTON_TEXT,
                                                          element_tag="button")
        sign_up_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT

        self.log.info ("Error message match to expected")

    def test_valid_fields_login(self, driver):
        base_helper=BaseHelpers (driver)
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
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value="test")
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        self.log.info ("Username field are filled with valid value and clear other")

        # Click on Sign Up button
        sign_up_button=base_helper.find_by_contains_text (text=LoginPageConstants.SIGN_UP_BUTTON_TEXT,
                                                          element_tag="button")
        sign_up_button.click ()
        self.log.info ("Clicked on 'Sign Up' button")
        sleep (2)

        # Verify error message
        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_USER_ALREADY_TAKEN_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_USER_ALREADY_TAKEN_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT

        self.log.info ('Error message match to expected')

    def test_valid_email_only(self, driver):
        base_helper=BaseHelpers (driver)
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
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value="test@test.ua")
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        self.log.info ("Clear required fields  and e-mail filled with valid values")

        # Click on Sign Up button
        sign_up_button=base_helper.find_by_contains_text (text=LoginPageConstants.SIGN_UP_BUTTON_TEXT,
                                                          element_tag="button")
        sign_up_button.click ()
        self.log.info ("Clicked on 'Sign Up' button")
        sleep (2)

        # Verify error message
        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MASSAGE_EMAIL_ALREADY_USED_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MASSAGE_EMAIL_ALREADY_USED_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT

        self.log.info ('Error message match to expected')

    def test_invalid_password_only(self, driver):
        base_helper=BaseHelpers (driver)
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
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH,
                                       value="test1234test1234test1234test1234test1234")
        self.log.info ("Clear required fields and add invalid password only")
        sleep (1)

        # Click on Sign Up button
        sign_up_button=base_helper.find_by_contains_text (text=LoginPageConstants.SIGN_UP_BUTTON_TEXT,
                                                          element_tag="button")
        sign_up_button.click ()
        self.log.info ("Clicked on 'Sign Up' button")
        sleep (2)

        # Verify error message
        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT

        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_PASSWORD_CANNOT_EXCEED_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_CANNOT_EXCEED_TEXT

        self.log.info ('Error message match to expected')

    def test_cyrillic_values_in_registration_form(self, driver):
        base_helper=BaseHelpers (driver)
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
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value="Александр")
        self.log.info ("Clear and field are filled with cyrillic username")
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value="тест@тест.юа")
        self.log.info ("Field are filled with cyrillic email")
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH,
                                       value="тест123тест123тест")
        self.log.info ("Field are filled with cyrillic password")

        # Click on Sign In button
        sign_up_button=base_helper.find_by_contains_text (text=LoginPageConstants.SIGN_UP_BUTTON_TEXT,
                                                          element_tag="button")
        sign_up_button.click ()
        self.log.info ("Clicked on 'Sign Up' button")
        sleep (2)

        # Verify error message
        error_message=base_helper.find_by_contains_text (LoginPageConstants.ERROR_MESSAGE_CYRILLIC_USER_NAME_TEXT)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_CYRILLIC_USER_NAME_TEXT

        self.log.info ('Error message match to expected')

    def test_cyrillic_values_in_login_form(self, driver):
        base_helper=BaseHelpers (driver)
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

        # Clear required fields and fill
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH,
                                       value="неправильное имя")
        base_helper.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH,
                                       value="парольпароль")

        # Click on Sign In button
        sign_in_button=base_helper.find_by_contains_text (text=LoginPageConstants.SIGN_IN_BUTTON_TEXT,
                                                          element_tag="button")
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")
        sleep (2)

        # Verify error message
        error_message=base_helper.find_by_contains_text (LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT)
        assert error_message.text == LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT
        self.log.info ("Error message match to expected")

    # def test_notification(self, driver):
    #     """
    #     - Open start page;
    #     - Find text UNDER "Remember Writing?" title;
    #     """
    #     # Open start page
    #     driver.get (BaseConstants.START_PAGE_URL)
    #     self.log.info ("Open Page")
    #
    #     # Find notification text
    #
    # def test_remember_writing(self, driver):
    #     """
    #     - Open start page;
    #     - Find text Complex app for testing - QA in header;
    #     """
    #     # Open start page
    #     driver.get (BaseConstants.START_PAGE_URL)
    #     self.log.info ("Open Page")
    #
    #     # Find text remember writing
