from pages.main_page import MainPage
# from pages.app_menu_page import RegionalSettingsPage
from time import sleep


def test_click_sing_in_button(browser):
    main_page = MainPage(browser)
    sleep(5)
    main_page.open_base_page()
    sleep(10)
    # main_page.open_regional_page()

