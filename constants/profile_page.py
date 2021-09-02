class ProfilePage:
    """Store constants related to Profile page"""

    HELLO_MESSAGE_TEXT="Hello {lower_username}, your feed is empty."
    HELLO_MESSAGE_XPATH=".//h2"
    HELLO_MESSAGE_USERNAME_XPATH=".//strong"

    SIGN_OUT_BUTTON_TEXT="Sign Out"
    SIGN_OUT_BUTTON_XPATH=f".//button[contains(text(), '{SIGN_OUT_BUTTON_TEXT}')]"

    TEXT_REMEMBER_CLASS="display-3"
    TEXT_REMEMBER_TEXT="Remember Writing?"
