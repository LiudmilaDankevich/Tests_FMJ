from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_EMAIL_FIELD = (By.XPATH, 'login-form[email]')
    LOCATOR_PASSWD_FIELD = (By.XPATH, 'login-form[email]')
    LOCATOR_REMEMBER_ME = (By.CLASS_NAME, 'ui-checkboxradio-icon ui-corner-all'
                                     ' ui-icon ui-icon-background ui-icon-check'
                                     ' ui-state-checked ui-state-hover"]')
    LOCATOR_SING_IN_BUTTON = (By.CLASS_NAME, 'btn btn_blue')
