import logging

from constants.profile_page import ProfilePage
from helpers.base import BaseHelpers


class ProfileHelpers (BaseHelpers):
    """Store helper methods related to profile page actions"""

    def __init__(self, driver):
        super ().__init__ (driver)
        self.log=logging.getLogger (__name__)

    def verify_hello_message(self, username):
        """Find hello message and verify in all possible ways"""
        hello_message=self.driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_XPATH)
        assert username.lower () in hello_message.text
        assert hello_message.text == ProfilePage.HELLO_MESSAGE_TEXT.format (lower_username=username.lower ())
        assert self.driver.find_element_by_xpath (ProfilePage.HELLO_MESSAGE_USERNAME_XPATH).text == username.lower ()
