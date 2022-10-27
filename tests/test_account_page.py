# from pages.main_page import MainPage
# from time import sleep
# from pages.account_page import AccountPage
#
# def test_registration_of_the_applicant(browser):
#
#     main_page = MainPage(browser)
#     main_page.open_base_page()
#     main_page.click_sing_in_button()
#     login_page = LoginPage(browser)
#     login_page.click_registration_applicant_button()
#     sleep(2)
#     registration_applicant_form = RegistrationApplicatorForm(browser)
#     registration_applicant_form.registration_of_the_applicant(
#         'Anna', 'Born', 'Born@gmail.com', '1111'
#     )