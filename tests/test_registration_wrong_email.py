import allure
from allure_commons.types import Severity

from qa_guru_22_final_tests_ui.pages.register_page import registration
from qa_guru_22_final_tests_ui.pages.open_page import page


@allure.epic('Registration')
@allure.tag('web')
@allure.label('owner', 'Product Specialist')
@allure.severity(Severity.BLOCKER)
@allure.title('Check registration with wrong email')
def test_registration_wrong_email():
    page.open_start_page()
    page.open_registration_form()
    registration.fill_form()
    registration.check_reg_error()
