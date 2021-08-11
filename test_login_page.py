"""Store tests related to star page"""
# from distutils.log import Log
from time import sleep

import pytest
# import self
from selenium import webdriver

from conftest import BaseTest


class TestLoginPage1 (BaseTest):

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
        yield driver
        driver.close ()

    def test_empty_fields_login(self, driver):
        """
        - Open start page;
        - Clear password and login fields;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields
        username = driver.find_element_by_xpath (".//input[@placeholder='Username']")
        username.clear ()
        password = driver.find_element_by_xpath (".//input[@placeholder='Password']")
        password.clear ()
        self.log.info ("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath (".//button[contains(text(), 'Sign In')]")
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")
        sleep (3)

        # Verify error message
        error_message = driver.find_element_by_xpath (".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info ("Error message match to expected")

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
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
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields and fill
        username = driver.find_element_by_xpath (".//input[@placeholder='Username']")
        username.clear ()
        # Add invalid value in username fields
        username.send_keys ("invalid name")
        password = driver.find_element_by_xpath (".//input[@placeholder='Password']")
        password.clear ()
        # Add invalid value in password fields
        password.send_keys ("098")
        self.log.info ("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath (".//button[contains(text(), 'Sign In')]")
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")
        sleep (2)

        # Verify error message
        error_message = driver.find_element_by_xpath (".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info ("Error message match to expected")

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
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
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields
        username = driver.find_element_by_xpath ('.//*[@id="username-register"]')
        username.clear ()
        email = driver.find_element_by_xpath ('.//*[@id="email-register"]')
        email.clear ()
        password = driver.find_element_by_xpath ('.//*[@id="password-register"]')
        password.clear ()
        self.log.info ("Clear required fields")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath ('.//*[@id="registration-form"]/button')
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[1]/div')
        assert error_message.text == 'Username must be at least 3 characters.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[2]/div')
        assert error_message.text == 'You must provide a valid email address.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[3]/div')
        assert error_message.text == 'Password must be at least 12 characters.'

        self.log.info ("Error message match to expected")

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
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
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields
        username = driver.find_element_by_xpath ('.//*[@id="username-register"]')
        username.clear ()
        email = driver.find_element_by_xpath ('.//*[@id="email-register"]')
        email.clear ()
        password = driver.find_element_by_xpath ('.//*[@id="password-register"]')
        password.clear ()
        self.log.info ("Clear required fields")

        # Add valid value in username field
        username.send_keys ("test")
        self.log.info ("Field are filled with valid values")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath ('.//*[@id="registration-form"]/button')
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[1]/div')
        assert error_message.text == 'That username is already taken.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[2]/div')
        assert error_message.text == 'You must provide a valid email address.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[3]/div')
        assert error_message.text == 'Password must be at least 12 characters.'

        self.log.info ('Error message match to expected')

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
        yield driver
        driver.close ()

    def testemptyfieldslogin3(self, driver):
        """
        - Open start page;
        - Clear username, e-mail, password fields;
        - Pick a valid email ;
        - Click on Sign In button;
        - Verify error message;
        """
        # Open start page
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields
        username = driver.find_element_by_xpath ('.//*[@id="username-register"]')
        username.clear ()
        email = driver.find_element_by_xpath ('.//*[@id="email-register"]')
        email.clear ()
        password = driver.find_element_by_xpath ('.//*[@id="password-register"]')
        password.clear ()
        self.log.info ("Clear required fields")

        # Add valid value in username field
        email.send_keys ("test@test.ua")
        self.log.info ("Field are filled with valid values")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath ('.//*[@id="registration-form"]/button')
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[1]/div')
        assert error_message.text == 'Username must be at least 3 characters.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[2]/div')
        assert error_message.text == 'That email is already being used.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[3]/div')
        assert error_message.text == 'Password must be at least 12 characters.'

        self.log.info ('Error message match to expected')

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
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
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields
        username = driver.find_element_by_xpath ('.//*[@id="username-register"]')
        username.clear ()
        email = driver.find_element_by_xpath ('.//*[@id="email-register"]')
        email.clear ()
        password = driver.find_element_by_xpath ('.//*[@id="password-register"]')
        password.clear ()
        self.log.info ("Clear required fields")

        # Add valid value in username field
        password.send_keys ("test1234test1234test1234test1234test1234test1234test1234")
        self.log.info ("Field are filled with valid values")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath ('.//*[@id="registration-form"]/button')
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[1]/div')
        assert error_message.text == 'Username must be at least 3 characters.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[2]/div')
        assert error_message.text == 'You must provide a valid email address.'

        error_message = driver.find_element_by_xpath ('.//*[@id="registration-form"]/div[3]/div')
        assert error_message.text == 'Password cannot exceed 50 characters'

        self.log.info ('Error message match to expected')

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
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
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields
        username = driver.find_element_by_xpath ('.//*[@id="username-register"]')
        username.clear ()
        email = driver.find_element_by_xpath ('.//*[@id="email-register"]')
        email.clear ()
        password = driver.find_element_by_xpath ('.//*[@id="password-register"]')
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
        sign_in_button = driver.find_element_by_xpath ('.//*[@id="registration-form"]/button')
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In' button")
        sleep (2)

        # Verify error message
        error_message = driver.find_element_by_xpath ('//*[@id="registration-form"]/div[1]/div')
        assert error_message.text == 'Username can only contain letters and numbers.'

        self.log.info ('Error message match to expected')

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
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
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

        # Clear required fields and fill
        username = driver.find_element_by_xpath (".//input[@placeholder='Username']")
        username.clear ()
        # Add invalid value in username fields
        username.send_keys ("неправильное имя")
        password = driver.find_element_by_xpath (".//input[@placeholder='Password']")
        password.clear ()
        # Add invalid value in password fields
        password.send_keys ("парольпароль")
        self.log.info ("Fields are filled with invalid values")

        # Click on Sign In button
        sign_in_button = driver.find_element_by_xpath (".//button[contains(text(), 'Sign In')]")
        sign_in_button.click ()
        self.log.info ("Clicked on 'Sign In'")
        sleep (2)

        # Verify error message
        error_message = driver.find_element_by_xpath (".//div[contains(text(), 'Invalid username / password')]")
        assert error_message.text == 'Invalid username / password'
        self.log.info ("Error message match to expected")

    # Find text - homework correct code
    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
        yield driver
        driver.close ()

    def test_Remember_Writing(self, driver):
        """
        - Open start page;
        - Find text UNDER "Remember Writing?" title;
        """
        # Open start page
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
        yield driver
        driver.close ()

    def get_notification_text(self):
        element = self.driver.find_element ('./html/body/div[2]/div[2]/div[1]/p').text
        print (element)

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
        yield driver
        driver.close ()

    def testrememberwriting(self, driver):
        """
        - Open start page;
        - Find text Complex app for testing - QA in header;
        """
        # Open start page
        driver.get ('https://qa-complex-app-for-testing.herokuapp.com/')
        self.log.info ("Open Page")

    @pytest.fixture (scope='class')
    def driver(self):
        driver = webdriver.Chrome (executable_path=r"C:\Users\Helen\PycharmProjects\QAComplexApp\drivers\chromedriver.exe")
        yield driver
        driver.close ()

    def getnotificationtext(self):
        element = self.driver.find_element ('./html/body/header/div/h4/a').text
        print (element)
