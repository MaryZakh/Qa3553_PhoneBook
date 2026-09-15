import pytest

from data.user_data import create_user, existing_user, invalid_email_user, invalid_password_user
from data.user_datasets import INVALID_LOGIN_USERS
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
def test_login_success(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()


    assert login_page.is_logged() is True




@pytest.mark.regression
@pytest.mark.parametrize("user_factory",INVALID_LOGIN_USERS)
def test_login_rejected(driver,user_factory):
    login_page = LoginPage(driver)
    user = user_factory()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()
#
# def test_login_with_wrong_email(driver):
#     login_page = LoginPage(driver)
#     user = invalid_email_user()
#
#     login_page.open_login_form()
#     login_page.fill_email(user.username)
#     login_page.fill_password(user.password)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
#
#
# def test_login_with_wrong_password(driver):
#     login_page = LoginPage(driver)
#     user = invalid_password_user()
#
#     login_page.open_login_form()
#     login_page.fill_email(user.username)
#     login_page.fill_password(user.password)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
#
#
# def test_login_unregistered_user(driver):
#     login_page = LoginPage(driver)
#     user = create_user()
#
#     login_page.open_login_form()
#     login_page.fill_email(user.username)
#     login_page.fill_password(user.password)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
