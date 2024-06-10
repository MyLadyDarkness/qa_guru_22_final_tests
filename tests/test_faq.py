from selene import browser, by, have

from pages.faq import faq
from pages.open_page import page


def test_faq():
    page.open_faq()
    faq.click_faq_item()
    faq.check_text()
