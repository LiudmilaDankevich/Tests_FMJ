from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_EMAIL_FIELD = (By.NAME, 'login-form[email]')
    LOCATOR_PASSWD_FIELD = (By.ID, 'login-form__password')
    LOCATOR_REMEMBER_ME = (By.CLASS_NAME, 'ui-checkboxradio-icon-space')
    LOCATOR_SING_IN_BUTTON = (By.XPATH, '//input[@value="Войти"]')
