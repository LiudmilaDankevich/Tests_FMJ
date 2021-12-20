from pages.base_page import BasePage
from locator.create_resume_locator import CreateResumePageLocator
from time import sleep


class PersonalAccountPage(BasePage):
    def create_a_resume(self):
        create_a_resume_click = self.find_element(
            CreateResumePageLocator.LOCATOR_CREATE_RESUME_CLICK
        )
        create_a_resume_click.click()

    def should_be_personal_account_page(self):

        personal_account_text = self.find_element(CreateResumePageLocator.LOCATOR_CREATE_RESUME_TEXT).text
        check_text = "Создать резюме"
        assert personal_account_text == check_text, f'Text on UI {personal_account_text} is not eq {check_text}'


    # def change_the_number_of_duck(self, number):
    #     change_the_number_of_duck = self.find_element(
    #         RubberDuckPageLocator.LOCATOR_QUANTITY_DUCK_FIELD
    #     )
    #     change_the_number_of_duck.click()
    #     change_the_number_of_duck.clear()
    #     change_the_number_of_duck.send_keys(number)
    #
    # def click_add_to_cart(self):
    #     add_to_cart = self.find_element(
    #         RubberDuckPageLocator.LOCATOR_ADD_TO_CART_BUTTON
    #     )
    #     add_to_cart.click()
    #     sleep(5)
    #
    # def click_cart(self):
    #     click_cart_order = self.find_element(
    #         RubberDuckPageLocator.LOCATOR_CURT_BUTTON
    #     )
    #     click_cart_order.click()
    #

