from pages.main_page import MainPage
from time import sleep

def open_base_page(browser):
   main_page = MainPage(browser)
   main_page.open_base_page()
   # main_page.open_header_page()
   main_page.should_be_header_logo()
