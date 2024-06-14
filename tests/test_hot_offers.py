import allure
from allure_commons.types import Severity

from qa_guru_22_final_tests_ui.pages.hot_offers_page import hot_offers
from qa_guru_22_final_tests_ui.pages.open_page import page


@allure.story('Hot offers')
@allure.tag('web')
@allure.label('owner', 'Project Manager')
@allure.severity(Severity.MINOR)
@allure.title('Check Hot offers loading')
def test_hot_offer():
    page.open_start_page()
    hot_offers.load_more()
    hot_offers.check_loaded()
