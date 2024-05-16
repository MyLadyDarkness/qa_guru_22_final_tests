import allure
from selene import browser
from data.analytics import Analytics
from model.pages.open_page import OpenPage
from utils import attach


def test_analytics_filter():
    page = OpenPage()

    with allure.step("Открывается страница аналитики"):
        page.open_analytics()

        analytics = Analytics()

    with allure.step("Вводятся данные для фильтрации"):
        analytics.filter_request("leod")

    with allure.step("Проверяется, что фильтр выдает хотя бы один релевантный результат"):
        analytics.check_filter("leod")
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)


def test_add_channel():
    page = OpenPage()

    with allure.step("Открывается страница аналитики"):
        page.open_analytics()

    channel = Analytics()

    with allure.step("Открывается форма добавления канала"):
        channel.add_channel()

    with allure.step("Проверяется, что нельзя добавить канал без ссылки"):
        channel.check_add_channel()
        attach.add_screenshot(browser)
