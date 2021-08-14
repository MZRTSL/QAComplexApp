class LoginPageConstants:
    """Store constants related to Login Page"""

    # Sign Up
    SIGN_IN_USERNAME_XPATH=".//input[@id='username-register']"
    SIGN_UP_USERNAME_XPATH='.//*[@id="username-register"]'
    SIGN_UP_EMAIL_XPATH='.//*[@id="email-register"]'
    SIGN_UP_PASSWORD_XPATH='.//*[@id="password-register"]'
    SIGN_UP_BUTTON_XPATH='.//*[@id="registration-form"]/button'

    # Sign in
    SIGN_IN_SURNAME_XPATH=".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH=".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT="Sign In"

    # Message
    INVALID_LOGIN_MESSAGE_TEXT='Invalid username / password'
    EMPTY_USERNAME_IN_REGISTRATION_FORM_TEXT="Username must be at least 3 characters."
    EMPTY_USERNAME_IN_REGISTRATION_FORM_XPATH='.//*[@id="registration-form"]/div[1]/div'
    EMPTY_EMAIL_IN_REGISTRATION_FORM_TEXT='You must provide a valid email address.'
    EMPTY_EMAIL_IN_REGISTRATION_FORM_XPATH='.//*[@id="registration-form"]/div[2]/div'
    EMPTY_PASSWORD_IN_REGISTRATION_FORM_TEXT='Password must be at least 12 characters.'
    EMPTY_PASSWORD_IN_REGISTRATION_FORM_XPATH='.//*[@id="registration-form"]/div[3]/div'
    USER_ALREADY_TAKEN_TEXT='That username is already taken.'
    USER_ALREADY_TAKEN_XPATH='.//*[@id="registration-form"]/div[1]/div'
    EMAIL_ALREADY_USED_TEXT='That email is already being used.'
    EMAIL_ALREADY_USED_XPATH='.//*[@id="registration-form"]/div[2]/div'
    PASSWORD_MORE_CHARACTERS_TEXT='Password cannot exceed 50 characters'
    PASSWORD_MORE_CHARACTERS_XPATH='.//*[@id="registration-form"]/div[3]/div'
    CYRRILIC_VALUE_MESSAGE_TEXT='Username can only contain letters and numbers.'
    CYRRILIC_VALUE_MESSAGE_XPATH='//*[@id="registration-form"]/div[1]/div'
