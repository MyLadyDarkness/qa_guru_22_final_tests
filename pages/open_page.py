import allure
from selene import browser


class OpenPage:

    def open_start_page(self):
        with allure.step("Открывается стартовая страница"):
            browser.open('/')
        return self

    def open_knowledge_base(self):
        with allure.step("Переход в базу знаний"):
            browser.element('[href*="help.telega"]').click()
        return self

    def open_registration_form(self):
        with allure.step("Открывается форма регистрации"):
            browser.element('.btn.hover-orange.js_open_registration').click()
        return self

    def open_login_form(self):
        with allure.step("Открывается форма входа"):
            browser.element('.enter.js_login').element('span').click()
        return self

    def open_analytics(self):
        with allure.step("Открывается страница аналитики"):
            browser.open('/analytics')
        return self


page = OpenPage()
