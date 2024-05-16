import allure

from data.knowledge_search import BaseSearch
from model.pages.open_page import OpenPage


def test_knowledge_base():
    search_value = "баланс"

    page = OpenPage()

    with allure.step("Открывается стартовая страница"):
        page.open_start_page()

    with allure.step("Переход в базу знаний"):
        page.open_knowledge_base()

    base_search = BaseSearch()

    with allure.step("Поиск в базе знаний по заданному запросу"):
        base_search.search_request(search_value)

    with allure.step("Появление капчи, провеяющей, ввел запрос человек или робот"):
        base_search.check_search_security()
