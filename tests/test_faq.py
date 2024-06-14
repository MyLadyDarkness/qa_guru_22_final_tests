import allure
from allure_commons.types import Severity

from telega_project_tests_ui.pages.faq_page import faq
from telega_project_tests_ui.pages.open_page import page


@allure.feature('FAQ')
@allure.tag('web')
@allure.label('owner', 'Product Specialist')
@allure.severity(Severity.MINOR)
@allure.title('Check text in FAQ')
def test_faq():
    page.open_faq()
    faq.click_faq_item()
    faq.check_text()
