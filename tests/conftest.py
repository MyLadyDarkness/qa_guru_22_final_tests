import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

options = Options()
selenoid_capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.base_url = 'https://telega.in'
    browser.config.window_height = 1500
    browser.config.window_width = 1500
    yield
    browser.quit()


options.capabilities.update(selenoid_capabilities)
driver = webdriver.Remote(
    command_executor=selenoid_url,
    options=options)

browser.config.driver = driver
