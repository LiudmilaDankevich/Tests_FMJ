from selenium.webdriver.common.by import By

class RegistrationApplicantLocator:
    LOCATOR_FIRST_NAME_FIELD = (By.NAME, 'applicant-register[nameFirst]')
    LOCATOR_LAST_NAME_FIELD = (By.NAME, 'applicant-register[nameLast]')
    LOCATOR_EMAIL_FIELD = (By.NAME, 'applicant-register[email]')
    LOCATOR_PASSWD_FIELD = (By.NAME, 'applicant-register[password]')
    LOCATOR_RADIO_BUTTON_ONE = (By. XPATH, '//*[@id="web-forms__collection_dd_ag1__item"]/label/span[1]')
    LOCATOR_RADIO_BUTTON_TWO = (By.XPATH, '//*[@id="web-forms__collection_dd_ag2__item"]/label/span[1]')
    LOCATOR_RADIO_BUTTON_THREE = (By.XPATH, '//*[@id="web-forms__collection_dd_ag3__item"]/label/span[1]')
    LOCATOR_RADIO_BUTTON_FOUR = (By.XPATH, '//*[@id="web-forms__collection_dd_ag4__item"]/label/span[1]')
    LOCATOR_REGISTRATION_BUTTON = (By.XPATH, '//*[@id="applicant-register-button"]')