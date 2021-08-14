import logging
from time import sleep

from selenium.webdriver.common.by import By

from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from helpers.base import BaseHelpers


class LoginHelpers (BaseHelpers):
    """Store helper methods related to login page actions"""

    def __init__(self, driver):
        super ().__init__ (driver)
        self.log=logging.getLogger (__name__)

    def login(self, username, password):
        """Login using provided credentials"""
        # Clear required fields and fill
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.log.debug ("Fields are filled with invalid values")

        # Click on Sign In button
        self.find_by_contains_text (text=LoginPageConstants.SIGN_IN_BUTTON_TEXT, element_tag="button").click ()
        self.log.info ("Clicked on 'Sign In'")

    def register_user(self, username, email, password):
        """Fill required fields and press button"""

        # Open start page
        self.driver.get (BaseConstants.START_PAGE_URL)
        self.log.debug ("Open page")

        # Fill fields
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=username)
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=email)
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password)
        self.log.debug ("Fields were filled")
        sleep (1)

        # Click on Sign Up button
        self.driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH).click ()
        sleep (1)

        return username, email, password

    def verify_error_message(self, text):
        """Find error message and verify text"""
        error_message=self.find_by_contains_text (text)
        assert error_message.text == text
