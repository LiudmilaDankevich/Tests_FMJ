from pages.base_page import BasePage
from locator.main_page_locator import MainPageLocator


class MainPage(BasePage):

    # def open_header_page(self):
    #     regional_change_button = self.find_element(
    #         MainPageLocator.LOCATOR_HEADER_LOGO
    #     )
    #     regional_change_button.click()
    def should_be_header_logo(self):
        header_logo_text = self.find_element(MainPageLocator.LOCATOR_HEADER_LOGO).text
        header_logo = 'praca.by'
        assert header_logo_text == header_logo, f'Text on UI {header_logo_text} is not eq {header_logo}'
