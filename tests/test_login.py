from pages.login import login
from pages.open_page import page


def test_login():
    page.open_start_page()
    page.open_login_form()
    login.submit_form()
    login.check_login_error()
