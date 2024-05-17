import allure
from selene import browser, have


class BaseSearch:

    def search_request(self, search_request):
        with allure.step("Поиск в базе знаний по заданному запросу"):
            browser.element('#query[name=query]').type(search_request)
            browser.element('#query[name=query]').press_enter()
        return self

    def check_search_results(self, search_request):
        with allure.step("Проверяется, что фильтр выдает хотя бы один релевантный результат"):
            browser.all('.results-list-item-link').first.should(have.text(search_request))
        return self


search = BaseSearch()
