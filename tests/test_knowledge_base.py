import time

import allure
from selene import browser, have

from utils import attach
from data.knowledge_search import BaseSearch
from model.pages.open_page import OpenPage


def test_knowledge_base():
    search_value = "баланс"

    page = OpenPage()

    with allure.step("Открывается стартовая страница"):
        page.open_start_page()

    with allure.step("Переход в базу знаний"):
        browser.element('a[href="https://help.telega.in/hc/ru"]').click()

    with allure.step("Поиск в базе знаний по заданному запросу"):
        browser.element('#query[name=query]').type(search_value)
        browser.element('#query[name=query]').press_enter()

    with allure.step("Поиск в базе знаний по заданному запросу"):
        browser.all('.results-list-item-link').first.should(have.text(search_value))


    # with allure.step("Открывается стартовая страница"):
    #     page.open_start_page()
    #
    # with allure.step("Переход в базу знаний"):
    #     page.open_knowledge_base()
    #
    # base_search = BaseSearch()
    #
    # with allure.step("Поиск в базе знаний по заданному запросу"):
    #     base_search.search_request(search_value)
    #     attach.add_screenshot(browser)
    #
    # #time.sleep(50)
    # with allure.step("Появление капчи, провеяющей, ввел запрос человек или робот"):
    #     base_search.check_search_security()
    #     attach.add_screenshot(browser)
