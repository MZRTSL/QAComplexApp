import logging

from selenium.webdriver.common.by import By

from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers


class ProfileHelpers (BaseHelpers):
    """Store helper methods related to profile page actions"""

    def __init__(self, driver):
        super ().__init__ (driver)
        self.log=logging.getLogger (__name__)

    def verify_hello_message(self, username):
        """Find hello message and verify in all possible ways"""
        self.wait_for_text (locator_type=By.XPATH, locator=ProfilePage.HELLO_MESSAGE_XPATH,
                            text=ProfilePage.HELLO_MESSAGE_TEXT.format (lower_username=username.lower ()))
        assert self.wait_until_element_find (locator_type=By.XPATH,
                                             locator=ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username.lower ()
