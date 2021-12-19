from pages.main_page import MainPage
# from pages.app_menu_page import RegionalSettingsPage
from time import sleep
from pages.login_in_page import LoginPage


def test_click_sing_in_button(browser):
    main_page = MainPage(browser)
    sleep(2)
    main_page.open_base_page()
    sleep(2)
    main_page.click_sing_in_button()
    # main_page.open_regional_page()
    login_page = LoginPage(browser)
    login_page.login('liud@gmail.com', '1111')

# def login_in_form(browser):
#     main_page = MainPage(browser)
#     main_page.open_base_page()
#     sleep(5)
#     login_page = LoginPage(browser)
#     sleep(5)
#     login_page.login('liud@gmail.com', '1111')
#     sleep(5)

