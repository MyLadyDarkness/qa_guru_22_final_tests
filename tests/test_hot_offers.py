from pages.hot_offers import hot_offers
from pages.open_page import page


def test_hot_offer():
    page.open_start_page()
    hot_offers.load_more()
    hot_offers.check_loaded()
