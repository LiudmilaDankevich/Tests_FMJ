from selenium.webdriver.common.by import By


class CreateResumePageLocator:
    LOCATOR_CREATE_RESUME_CLICK = (By.CLASS_NAME, 'btn btn_blue-transparent btn_large')
    LOCATOR_CREATE_RESUME_TEXT = (By.LINK_TEXT, 'Создать резюме')
    # LOCATOR_REMEMBER_ME = (By.CLASS_NAME, 'ui-checkboxradio-icon-space')
    # LOCATOR_SING_IN_BUTTON = (By.XPATH, '//input[@value="Войти"]')
