from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_EMAIL_FIELD = (By.NAME, 'login-form[email]')
    LOCATOR_PASSWD_FIELD = (By.ID, 'login-form__password')
    LOCATOR_REMEMBER_ME = (By.CLASS_NAME, 'ui-checkboxradio-icon-space')
    LOCATOR_SING_IN_BUTTON = (By.XPATH, '//input[@value="Войти"]')
    LOCATOR_REGISTRATION_APPLICANT_BUTTON = (
        By.XPATH, '//*[@id="js-login-modal"]/div/div/div/section/div[2]/div/div[1]/a'
    )
    LOCATOR_LOGIN_FORM =(By.XPATH,'//*[@id="js-login-modal"]/div/div/div/section/div[1]')
    LOCATOR_AUTH_TEXT = (By.XPATH,
                         '//*[@id="js-login-modal"]/div/div/div/section/div[1]/div[1]'
                         )

