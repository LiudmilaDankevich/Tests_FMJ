from pages.main_page import MainPage
# from pages.app_menu_page import RegionalSettingsPage
from time import sleep
from pages.login_in_page import LoginPage


def test_click_sing_in_button(browser):
    main_page = MainPage(browser)
    sleep(2)
    main_page.open_base_page()
    sleep(2)
    main_page.should_be_main_page()
    # confirm = browser.switch_to.alert
    # confirm.accept()

