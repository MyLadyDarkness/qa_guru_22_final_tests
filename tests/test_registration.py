from pages.register import registration
from pages.open_page import page


def test_registration():
    page.open_start_page()
    page.open_registration_form()
    registration.fill_form()
    registration.check_reg_error()
