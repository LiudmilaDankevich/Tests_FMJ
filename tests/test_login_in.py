from pages.main_page import MainPage
# from pages.app_menu_page import RegionalSettingsPage
from time import sleep
from pages.login_in_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


def test_click_sing_in_button(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.click_sing_in_button()
    sleep(2)
    login_page = LoginPage(browser)
    sleep(2)
    login_page.login('liud@gmail.com', '1111')
    sleep(2)
    # personal_account_page = PersonalAccountPage(browser)
    # sleep(2)
    # personal_account_page.should_be_personal_account_page()
