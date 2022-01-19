from selenium.webdriver.common.by import By

class MainPageLocator:
    LOCATOR_SING_IN_BUTTON = (By.LINK_TEXT, 'Вход и регистрация')
    LOCATOR_FIND_JOB_FORM = (
        By.NAME, "search[query]")
    LOCATOR_MAIN_PAGE_TEXT = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/h1')
    # LOCATOR_REGISTRATION_APPLICANT_BUTTON
    # LOCATOR_CONFIRM_ALERT = (By.XPATH, '/html/body/script[1]')