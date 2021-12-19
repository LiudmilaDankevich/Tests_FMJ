from pages.login_in_page import LoginPage
from pages.main_page import MainPage

from time import sleep


def login_in_form(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    login_page = LoginPage(browser)
    login_page.login('liud@gmail.com', '1111')