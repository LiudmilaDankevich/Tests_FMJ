from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_EMAIL_FIELD = (By.NAME, 'login-form[email]')
    LOCATOR_PASSWD_FIELD = (By.ID, 'login-form__password')
    LOCATOR_REMEMBER_ME = (By.CLASS_NAME, 'ui-checkboxradio-icon ui-corner-all'
                                     ' ui-icon ui-icon-background ui-icon-check'
                                     ' ui-state-checked ui-state-hover"]')
    LOCATOR_SING_IN_BUTTON = (By.XPATH, '//input[@value="Войти"]')
