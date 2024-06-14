import allure
from allure_commons.types import Severity

from qa_guru_22_final_tests_ui.pages.analytics_page import analytics
from qa_guru_22_final_tests_ui.pages.open_page import page
import pytest


@allure.feature('Analytic Filter')
@allure.tag('web')
@allure.label('owner', 'Product Specialist')
@allure.severity(Severity.NORMAL)
@allure.title('Check filter')
@pytest.mark.parametrize('input_data', ['leod', 'ria', 'mir'])
def test_analytics_filter(input_data):
    page.open_analytics()
    analytics.filter_request(input_data)
    analytics.check_filter(input_data)


@allure.feature('Add new channel to Analytic')
@allure.tag('web')
@allure.label('owner', 'Project Manager')
@allure.severity(Severity.NORMAL)
@allure.title('Try add channel without link')
def test_add_channel():
    page.open_analytics()
    analytics.add_channel()
    analytics.check_add_channel_no_link()
