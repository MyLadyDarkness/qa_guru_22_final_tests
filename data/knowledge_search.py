from selene import browser, have


class BaseSearch:

    def search_request(self, search_request):
        browser.element('input[type=search]').type(search_request)
        browser.element('input[type=search]').press_enter()

    def check_search_security(self):
        browser.element('#challenge-running').should(have.text("Подтвердите, что вы человек"))
