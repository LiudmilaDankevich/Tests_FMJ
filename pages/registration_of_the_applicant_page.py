from pages.main_page import MainPage
from pages.base_page import BasePage
from locator.registration_of_the_applicant_locator import RegistrationApplicantLocator
from time import sleep

class RegistrationApplicatorForm(BasePage):
    def registration_of_the_applicant(self, first_name, last_name, email, passwd):
        first_name_applicant_field = self.find_element(
            RegistrationApplicantLocator.LOCATOR_FIRST_NAME_FIELD
        )
        first_name_applicant_field.send_keys(first_name)

        last_name_applicant_field = self.find_element(
            RegistrationApplicantLocator.LOCATOR_LAST_NAME_FIELD
        )
        last_name_applicant_field.send_keys(last_name)

        email_applicant_field = self.find_element(
            RegistrationApplicantLocator.LOCATOR_EMAIL_FIELD
        )
        email_applicant_field.send_keys(email)

        passwd_applicant_field = self.find_element(
            RegistrationApplicantLocator.LOCATOR_PASSWD_FIELD
        )
        passwd_applicant_field.send_keys(passwd)

        radio_button_one = self.find_element(
            RegistrationApplicantLocator.LOCATOR_RADIO_BUTTON_ONE
        )
        radio_button_one.click()

        radio_button_two = self.find_element(
            RegistrationApplicantLocator.LOCATOR_RADIO_BUTTON_TWO
        )
        radio_button_two.click()

        radio_button_three = self.find_element(
            RegistrationApplicantLocator.LOCATOR_RADIO_BUTTON_THREE
        )
        radio_button_three.click()

        radio_button_four = self.find_element(
            RegistrationApplicantLocator.LOCATOR_RADIO_BUTTON_FOUR
        )
        radio_button_four.click()




    # def employer_registration(self):