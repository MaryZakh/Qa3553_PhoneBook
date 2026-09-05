# from pages.registration_page import RegistrationPage
#
# VALID_EMAIL = "margo_12346@gmail.com"
# VALID_PASSWORD = "Mmar123456$"
# INVALID_EMAIL = "margo123gmail.com"
# INVALID_PASSWORD = "Mmar123"
#
#
# def test_registration_success(driver):
#     registration_page = RegistrationPage(driver)
#
#     registration_page.open_registration_form()
#     registration_page.fill_email(VALID_EMAIL)
#     registration_page.fill_password(VALID_PASSWORD)
#     registration_page.submit_registration()
#
#     assert registration_page.is_registered() is True
#
#
# def test_registration_wrong_email(driver):
#     registration_page = RegistrationPage(driver)
#
#     registration_page.open_registration_form()
#     registration_page.fill_email(INVALID_EMAIL)
#     registration_page.fill_password(VALID_PASSWORD)
#     registration_page.submit_registration()
#
#     assert "Wrong email or password format" in registration_page.get_alert_text()
#     registration_page.accept_alert()
#
# def test_registration_wrong_password(driver):
#     registration_page = RegistrationPage(driver)
#
#     registration_page.open_registration_form()
#     registration_page.fill_email(VALID_EMAIL)
#     registration_page.fill_password(INVALID_PASSWORD)
#     registration_page.submit_registration()
#
#     assert "Wrong email or password format" in registration_page.get_alert_text()
#     registration_page.accept_alert()
#
# def test_registration_exists_user(driver):
#     registration_page = RegistrationPage(driver)
#
#     registration_page.open_registration_form()
#     registration_page.fill_email("margo@gmail.com")
#     registration_page.fill_password("Mmar123456$")
#     registration_page.submit_registration()
#
#     assert registration_page.get_alert_text()=="User already exist"
#     registration_page.accept_alert()