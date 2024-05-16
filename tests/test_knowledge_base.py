import allure

from data.knowledge_search import BaseSearch
from model.pages.open_page import OpenPage


def test_knowledge_base():
    search_value = "баланс"

    page = OpenPage()
    search = BaseSearch()

    with allure.step("Открывается стартовая страница"):
        page.open_start_page()

    with allure.step("Переход в базу знаний"):
        page.open_knowledge_base()

    with allure.step("Поиск в базе знаний по заданному запросу"):
        search.search_request(search_value)

    with allure.step("Проверяется, что фильтр выдает хотя бы один релевантный результат"):
        search.check_search_results(search_value)