import logging

from selenium.webdriver.common.by import By

from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers, wait_until_ok


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
        self.wait_and_click (By.XPATH, LoginPageConstants.SIGN_IN_BUTTON_XPATH)
        self.log.info ("Clicked on 'Sign In'")

    @wait_until_ok (timeout=10)
    def click_sign_up_and_verify(self):
        """click on Sign In button and verify the result"""
        # Click on sign in button
        self.wait_and_click (By.XPATH, LoginPageConstants.SIGN_UP_BUTTON_XPATH)

        # Verify register success
        assert self.is_element_exists (By.XPATH, ProfilePage.SIGN_OUT_BUTTON_XPATH)

    def register_user(self, username, email, password):
        """
        - Open start page;
        - Clear username, email, password fields for Sing UP form;
        - Add information in registration from
        - Click on Sign up button;
        - Verify user registration successful
        """
        # Open start page
        self.driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # fill fields in Registration form
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=username)
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=email)
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password)
        self.log.debug ("Fields were filled")

        # Click on Sign Up for OurApp button
        self.click_sign_up_and_verify ()

        return username, email, password

    def fill_registration_form(self, username, email, password):
        """
                - Open start page;
                - Clear username, email, password fields for Sing UP form;
                - Add information in registration from
                - Click on Sign up button;
        """
        # Open start page
        self.driver.get (BaseConstants.START_PAGE_URL)
        self.log.info ("Open Page")

        # fill fields in Registration form
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_USERNAME_XPATH, value=username)
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_EMAIL_XPATH, value=email)
        self.fill_input_field (by=By.XPATH, locator=LoginPageConstants.SIGN_UP_PASSWORD_XPATH, value=password)
        self.log.debug ("Fields were filled")

        # Click on sign in button
        self.wait_and_click (By.XPATH, LoginPageConstants.SIGN_UP_BUTTON_XPATH)

    def verify_error_message(self, text):
        """Find error text and verify it"""
        assert self.is_text_exists (locator_type=By.XPATH, locator=f".//*[contains(text(), '{text}')]", text=text)
