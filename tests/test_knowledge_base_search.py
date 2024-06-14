import allure
from allure_commons.types import Severity

from qa_guru_22_final_tests_ui.pages.knowledge_search_page import search
from qa_guru_22_final_tests_ui.pages.open_page import page


@allure.epic('Knowledge base')
@allure.tag('web')
@allure.label('owner', 'Project Manager')
@allure.severity(Severity.NORMAL)
@allure.title('Check search in Knowledge base')
def test_knowledge_base_search():
    search_value = "баланс"
    page.open_start_page()
    page.open_knowledge_base()
    search.search_request(search_value)
    search.check_search_results(search_value)
