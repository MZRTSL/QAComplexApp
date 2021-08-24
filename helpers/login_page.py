import logging
from asyncio import sleep

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

        self.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_IN_PASSWORD_XPATH, value=password)
        sleep (1)
        self.log.debug ("Fields are filled with invalid values")

        # Click on Sign In button
        sign_up_button=self.find_by_contains_text (text=LoginPageConstants.SIGN_UP_BUTTON_TEXT, element_tag="button")
        sign_up_button.click ()
        self.log.info ("Clicked on 'Sign In' button")

    def test_registered_user(self, username, email, password):
        """
        - Open start page;
        - Clear username, email, password fields for Sing In form;
        - Add information in registration from
        - Click on Sign In button;
        - Verify user registration successful
        """
        # Open start page
        self.driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # fill fields in Registration form
        self.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=username)
        self.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=email)
        self.fill_input_fields (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password)
        sleep (1)

        # Click on Sign Up for OurApp button
        self.driver.find_element_by_xpath (LoginPageConstants.SIGN_UP_BUTTON_XPATH).click ()

        return username, email, password
