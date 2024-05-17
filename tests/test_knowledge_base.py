from pages.knowledge_search import search
from pages.open_page import page


def test_knowledge_base():
    search_value = "баланс"

    page.open_start_page()
    page.open_knowledge_base()
    search.search_request(search_value)
    search.check_search_results(search_value)