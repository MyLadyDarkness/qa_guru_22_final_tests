from pages.analytics import analytics
from pages.open_page import page


def test_analytics_filter():
    page.open_analytics()
    analytics.filter_request("leod")
    analytics.check_filter("leod")


def test_add_channel():
    page.open_analytics()
    analytics.add_channel()
    analytics.check_add_channel()
