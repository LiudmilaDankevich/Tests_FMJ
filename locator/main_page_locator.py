from selenium.webdriver.common.by import By

class MainPageLocator:
    LOCATOR_SING_IN_BUTTON = (By.LINK_TEXT, 'Вход и регистрация')
    LOCATOR_REGISTRATION_APPLICANT_BUTTON = (
        By.XPATH, '//*[@id="js-login-modal"]/div/div/div/section/div[2]/div/div[1]/a'
    )
