import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.base_url = 'https://telega.in'
    browser.config.window_height = 1500
    browser.config.window_width = 1500
    yield
    browser.quit()
