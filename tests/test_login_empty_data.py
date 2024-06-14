import allure
from allure_commons.types import Severity

from telega_project_tests_ui.pages.login_page import login
from telega_project_tests_ui.pages.open_page import page


@allure.epic('Login')
@allure.tag('web')
@allure.label('owner', 'Project Manager')
@allure.severity(Severity.CRITICAL)
@allure.title('Check login with empty data')
def test_login_empty_data():
    page.open_start_page()
    page.open_login_form()
    login.submit_form()
    login.check_login_error()
