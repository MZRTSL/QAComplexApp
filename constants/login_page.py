class LoginPageConstants:
    """Store constants related to Login Page"""

    # Sign in
    SIGN_IN_USERNAME_XPATH=".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH=".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT='Sign In'
    SIGN_IN_BUTTON_XPATH="/html/body/header/div/form/div/div[3]/button"

    SIGN_UP_USERNAME_XPATH='.//*[@id="username-register"]'
    SIGN_UP_EMAIL_XPATH='.//*[@id="email-register"]'
    SIGN_UP_PASSWORD_XPATH='.//*[@id="password-register"]'
    SIGN_UP_BUTTON_XPATH='.//*[@id="registration-form"]/button'
    SIGN_UP_BUTTON_TEXT='Sign up'

    # Messages
    HELLO_MESSAGE_XPATH='/html/body/div[2]/div[1]'
    SIGN_IN_EMPTY_FIELDS_LOGIN_XPATH=".//div[contains(text(), 'Invalid username / password')]"
    ERROR_MESSAGE_CYRILLIC_USER_NAME_XPATH='//*[@id="registration-form"]/div[1]/div'
    ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_XPATH='.//*[@id="registration-form"]/div[1]/div'
    ERROR_MESSAGE_EMAIL_FIELDS_XPATH='.//*[@id="registration-form"]/div[2]/div'
    ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_XPATH='.//*[@id="registration-form"]/div[3]/div'

    NOTIFICATION_XPATH='./html/body/div[2]/div[2]/div[1]/p'
    REMEMBER_WRITING_XPATH='./html/body/div[2]/div/div[1]/h1'

    # Texts
    HELLO_MESSAGE_TEXT="Invalid username / password"
    SIGN_IN_EMPTY_FIELDS_LOGIN_TEXT="Invalid username / password"
    ERROR_MESSAGE_CYRILLIC_USER_NAME_TEXT='Username can only contain letters and numbers.'
    ERROR_MESSAGE_EMPTY_USERNAME_FIELDS_TEXT='Username must be at least 3 characters.'
    ERROR_MESSAGE_EMAIL_FIELDS_TEXT='You must provide a valid email address.'
    ERROR_MASSAGE_EMAIL_ALREADY_USED_TEXT='That email is already being used.'
    ERROR_MESSAGE_PASSWORD_EMPTY_FIELDS_TEXT='Password must be at least 12 characters.'
    ERROR_MESSAGE_USER_ALREADY_TAKEN_TEXT='That username is already taken.'
    ERROR_MESSAGE_PASSWORD_CANNOT_EXCEED_TEXT='Password cannot exceed 50 characters'

    # Sign Out
    SIGN_OUT_BUTTON_XPATH="/html/body/header/div/div/form/button"

    # Find text
    HEADER_XPATH="/html/body/header/div/h4/a"
