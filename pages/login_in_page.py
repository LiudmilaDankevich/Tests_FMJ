from pages.base_page import BasePage
from pages.main_page import MainPage
from locator.login_in_locator import LoginPageLocator
from time import sleep


class LoginPage(BasePage):

    def login(self, email, passwd):
        email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        sleep(2)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_FIELD)
        passwd_field.send_keys(passwd)
        sleep(2)
        remember_me = self.find_element(LoginPageLocator.LOCATOR_REMEMBER_ME)
        remember_me.click()
        sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
        sing_in_button.click()