import logging
import time

import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_ok(timeout, period=0.25):
    """"""

    def act_decorator(target_func):
        logger=logging.getLogger (__name__)

        def wrapper(*args, **kwargs):
            must_end=time.time () + timeout
            while True:
                try:
                    return target_func (*args, **kwargs)
                except (WebDriverException, AssertionError, TimeoutException) as error:
                    error_name=error if str (error) else error.__class__.__name__
                    logger.debug ("Catch %s. Left %s seconds", error_name, (must_end - time.time ()))
                    if time.time () >= must_end:
                        logger.warning ("Waiting timed out after %s", timeout)
                        raise error
                    time.sleep (period)

        return wrapper

    return act_decorator


class BaseHelpers:
    """Store base helpers for texting"""

    def __init__(self, driver):
        self.driver=driver
        self.wait=WebDriverWait (self.driver, timeout=5)

    def is_element_exists(self, locator_type, locator):
        """Check if element present, return False if not otherwise True"""
        try:
            self.wait_until_element_find (locator_type, locator)
            return True
        except TimeoutException:
            return False

    def element_exists(self, locator_type, locator):
        """Check if element present, return False if not otherwise True"""
        try:
            self.wait_until_element_find (locator_type, locator)
            return True
        except TimeoutException:
            return False

    def is_text_exists(self, locator_type, locator, text):
        """Check if text present, return False if not otherwise True"""
        try:
            self.wait_for_text (locator_type, locator, text)
            return True
        except TimeoutException:
            return False

    def wait_for_text(self, locator_type, locator, text):
        """Wait until text appears"""
        self.wait.until (EC.text_to_be_present_in_element ((locator_type, locator), text))

    def wait_until_element_find(self, locator_type, locator):
        """Wait until element find and return it"""
        self.wait.until (EC.presence_of_element_located ((locator_type, locator)))
        return self.driver.find_element (by=locator_type, value=locator)

    def wait_and_click(self, locator_type, locator):
        """Wait until element clickable and click"""
        self.wait.until (EC.element_to_be_clickable ((locator_type, locator)))
        self.driver.find_element (by=locator_type, value=locator).click ()

    def fill_input_field(self, by, locator, value=""):
        """Find required element using by X. model, clear input field and enter the value"""
        field=self.wait_until_element_find (locator_type=by, locator=locator)
        field.clear ()
        field.send_keys (value)

    def find_by_contains_text(self, text, element_tag="*"):
        """Find element using XPATH contains function by text"""
        return self.wait_until_element_find (By.XPATH, f".//{element_tag}[contains(text(), '{text}')]")
