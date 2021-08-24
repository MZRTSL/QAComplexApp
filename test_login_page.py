"""Store tests related to star page"""
# from distutils.log import Log
from time import sleep

import pytest
from selenium import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage


class TestLoginPage1 (BaseTest):

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    @pytest.fixture (scope="function")
    def logout(self, driver):
        yield
        driver.find_element_by_xpath (ProfilePage.SIGN_OUT_BUTTON_XPATH)
        sleep (1)

    @pytest.fixture (scope="function")
    def register(self, driver, logout):
        registered_user=self.registered_user (driver, logout)
        driver.find_element_by_xpath (ProfilePage.SIGN_OUT_BUTTON_XPATH)
        sleep (1)
        return registered_user

    def test_empty_fields_login(self, driver):
        """
        - Open start page;
        - Clear password and login fields;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear required fields
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        username.clear ()
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        password.clear ()
        self.log.info ("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")
        sleep (3)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_XPATH)
        assert error_message.text == LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT
        self.log.info ("Error message match to expected")

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def testemptyfieldslogin(self, driver):
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

        # Clear required fields and fill
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        username.clear ()
        # Add invalid value in username fields
        username.send_keys ("invalid name")
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        password.clear ()
        # Add invalid value in password fields
        password.send_keys ("098")
        self.log.info ("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")
        sleep (2)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_XPATH)
        assert error_message.text == LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT
        self.log.info ("Error message match to expected")
        sleep (1)

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def testemptyfieldslogin1(self, driver):
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
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear ()
        email=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        email.clear ()
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear ()
        self.log.info ("Clear required fields")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT

        self.log.info ("Error message match to expected")

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def testemptyfieldslogin2(self, driver):
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

        # Clear required fields
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear ()
        email=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        email.clear ()
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear ()
        self.log.info ("Clear required fields")

        # Add valid value in username field
        username.send_keys ("test")
        self.log.info ("Field are filled with valid values")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_USER_ALREADY_TAKEN_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT

        self.log.info ('Error message match to expected')

    def testemptyfieldslogin3(self, driver):
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
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear ()
        email=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        email.clear ()
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear ()
        self.log.info ("Clear required fields")

        # Add valid value in username field
        email.send_keys ("test@test.ua")
        self.log.info ("Field are filled with valid values")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MASSAGE_EMAIL_ALREADY_USED_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT

        self.log.info ('Error message match to expected')

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def testemptyfieldslogin4(self, driver):
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
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear ()
        email=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        email.clear ()
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear ()
        self.log.info ("Clear required fields")

        # Add valid value in username field
        password.send_keys ("test1234test1234test1234test1234test1234test1234test1234")
        self.log.info ("Field are filled with valid values")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_EMAIL_FIELDS_TEXT

        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_PASSWORD_CANNOT_EXCEED_TEXT

        self.log.info ('Error message match to expected')

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def test_cyrillic_values(self, driver):
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
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear ()
        email=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        email.clear ()
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear ()
        self.log.info ("Clear required fields")

        # Add a Cyrillic user name, e-mail, password
        username.send_keys ("Александр")
        self.log.info ("Field are filled with cyrillic username")
        email.send_keys ("тест@тест.юа")
        self.log.info ("Field are filled with cyrillic email")
        password.send_keys ("тест123тест123тест")
        self.log.info ("Field are filled with cyrillic password")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.ERROR_MESSAGE_CYRILLIC_USER_NAME_XPATH)
        assert error_message.text == LoginPageConstants.ERROR_MESSAGE_CYRILLIC_USER_NAME_TEXT

        self.log.info ('Error message match to expected')

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def testcyrillicvalues(self, driver):
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
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        username.clear ()
        # Add invalid value in username fields
        username.send_keys ("неправильное имя")
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        password.clear ()
        # Add invalid value in password fields
        password.send_keys ("парольпароль")
        self.log.info ("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")
        sleep (2)

        # Verify error message
        error_message=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_XPATH)
        assert error_message.text == LoginPageConstants.SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT
        self.log.info ("Error message match to expected")

    # Find text - homework correct code
    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def test_Remember_Writing(self, driver):
        """
        - Open start page;
        - Find text UNDER "Remember Writing?" title;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def get_notification_text(self):
        element=self.driver.find_element ('./html/body/div[2]/div[2]/div[1]/p').text
        print (element)

    @pytest.fixture (scope='class')
    def driver(self):
        driver=webdriver.Chrome (executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close ()

    def testrememberwriting(self, driver):
        """
        - Open start page;
        - Find text Complex app for testing - QA in header;
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

    def registered_user(self, driver, logout):
        """
        - Open start page;
        - Clear username, email, password fields for Sing In form;
        - Add information in registration from
        - Click on Sign In button;
        - Verify user registration successful
        """
        # Open start page
        driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # Clear and fill username, email, password Sing In form;
        username_value=f"Name{self.variety}"
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_USERNAME_XPATH)
        username.clear ()
        username.send_keys (username_value)

        email_value=f"user{self.variety}@gmail.com"
        email=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_EMAIL_XPATH)
        email.clear ()
        email.send_keys (email_value)

        password_value=f"Password{self.variety}"
        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_PASSWORD_XPATH)
        password.clear ()
        password.send_keys (password_value)

        # Click on Sign Up for OurApp button
        sign_up_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH)
        sign_up_button.click ()
        self.log.info ("Click on Sign Up for OurApp button")
        sleep (1)

        return username_value, email_value, password_value

        # Verify Hello message
        # noinspection PyUnreachableCode
        hello_message=driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_XPATH)
        assert username_value.lower () in hello_message.text
        assert hello_message.text == ProfilePage.HELLO_MESSAGE_TEXT.format (lower_username=username_value.lower ())
        assert driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username_value.lower ()
        self.log.info ("Registration was success and verified")
        sleep (1)

    def test_login(self, register, driver, logout):
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

        # Clear and fill username, email, password Sing In form;
        username=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_USERNAME_XPATH)
        username.clear ()
        username.send_keys (username_value)

        password=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_PASSWORD_XPATH)
        password.clear ()
        password.send_keys (password_value)

        # Click on Sign Up for OurApp button
        sign_in_button=driver.find_element_by_xpath (LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click ()
        self.log.info ("Click on Sign In")
        sleep (1)

        # Verify register success
        hello_message=driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_XPATH)
        assert username_value.lower () in hello_message.text
        assert driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username_value.lower ()
        self.log.info ("Registration was success and verified")
        sleep (1)
