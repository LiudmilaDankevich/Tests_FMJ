from pages.base_page import BasePage
from pages.main_page import MainPage
from locator.main_page_locator import MainPageLocator
from locator.login_in_locator import LoginPageLocator
from time import sleep


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.login_form_is_present()
        self.auth_text_is_present()

    def login_form_is_present(self):
        self.find_element(LoginPageLocator.LOCATOR_LOGIN_FORM)

    def auth_text_is_present(self):
        auth_text = self.find_element(LoginPageLocator.LOCATOR_AUTH_TEXT).text
        check_text = 'Вход'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'

    def login(self, email, passwd):
        email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        sleep(2)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_FIELD)
        passwd_field.send_keys(passwd)
        sleep(2)
        # remember_me = self.find_element(LoginPageLocator.LOCATOR_REMEMBER_ME)
        # remember_me.click()
        sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
        sing_in_button.click()

    def click_registration_applicant_button(self):
        registration_applicant_button = self.find_element(
            LoginPageLocator.LOCATOR_REGISTRATION_APPLICANT_BUTTON
        )
        registration_applicant_button.click()
