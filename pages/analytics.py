import allure
from selene import browser, have


@allure.feature("Аналитика")
class Analytics:

    def filter_request(self, filter_request):
        with allure.step("Вводятся данные для фильтрации"):
            browser.element("#filter_search").type(filter_request)

    def check_filter(self, filter_request):
        with allure.step("Проверяется, что фильтр выдает хотя бы один релевантный результат"):
            browser.all(".item-info-link").first.should(have.text(filter_request))

    def add_channel(self):
        with allure.step("Открывается форма добавления канала"):
            browser.element('[href*="add_new_channel"]').click()
            browser.element('.submit').click()

    def check_add_channel(self):
        with allure.step("Проверяется, что нельзя добавить канал без ссылки"):
            browser.element('.error_text').should(have.text("Поле не может быть пустым"))


analytics = Analytics()
