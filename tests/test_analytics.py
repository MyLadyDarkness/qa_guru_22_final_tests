from pages.analytics import analytics
from pages.open_page import page
import pytest
from utils.check_exceptions import check_exceptions


@pytest.mark.skipif(check_exceptions(), reason="Exception in Selenoid, need rerun")
def test_analytics_filter():
    page.open_analytics()
    analytics.filter_request("leod")
    analytics.check_filter("leod")


@pytest.mark.skipif(check_exceptions(), reason="Exception in Selenoid, need rerun")
def test_add_channel():
    page.open_analytics()
    analytics.add_channel()
    analytics.check_add_channel()
