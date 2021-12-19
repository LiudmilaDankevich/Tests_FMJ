from pages.base_page import BasePage
from locator.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def open_regional_page(self):
        sing_in_button = self.find_element(
            MainPageLocator.LOCATOR_SING_IN_BUTTON
        )
        sing_in_button.click()