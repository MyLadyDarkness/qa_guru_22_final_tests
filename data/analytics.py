from selene import browser, have


class Analytics:

    def filter_request(self, filter_request):
        browser.element("#filter_search").type(filter_request)

    def check_filter(self, filter_request):
        browser.all(".item-info-link").first.should(have.text(filter_request))

    def add_channel(self):
        browser.element('div[href="/analytics/add_new_channel"]').click()
        browser.element('.submit').click()

    def check_add_channel(self):
        browser.element('.error_text').should(have.text("Поле не может быть пустым"))
