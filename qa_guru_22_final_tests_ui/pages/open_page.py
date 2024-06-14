import allure
from selene import browser


@allure.epic("Открытие страниц сайта")
class OpenPage:

    @allure.tag("smoke", "regression")
    @allure.label("priority", "high")
    @allure.severity(allure.severity_level.CRITICAL)
    def open_start_page(self):
        with allure.step("Открывается стартовая страница"):
            browser.open('/')
        return self

    @allure.tag("regression")
    @allure.label("priority", "medium")
    @allure.severity(allure.severity_level.NORMAL)
    def open_knowledge_base(self):
        with allure.step("Переход в базу знаний"):
            browser.element('[href*="help.telega"]').click()
        return self

    @allure.tag("smoke", "regression")
    @allure.label("priority", "high")
    @allure.severity(allure.severity_level.CRITICAL)
    def open_registration_form(self):
        with allure.step("Открывается форма регистрации"):
            browser.element('.btn.hover-orange.js_open_registration').click()
        return self

    @allure.tag("smoke", "regression")
    @allure.label("priority", "high")
    @allure.severity(allure.severity_level.CRITICAL)
    def open_login_form(self):
        with allure.step("Открывается форма входа"):
            browser.element('.enter.js_login').element('span').click()
        return self

    @allure.tag("regression")
    @allure.label("priority", "low")
    @allure.severity(allure.severity_level.MINOR)
    def open_analytics(self):
        with allure.step("Открывается страница аналитики"):
            browser.open('/analytics')
        return self

    @allure.tag("regression")
    @allure.label("priority", "medium")
    @allure.severity(allure.severity_level.NORMAL)
    def open_faq(self):
        with allure.step("Открывается страница FAQ"):
            browser.open('/faq')
        return self


page = OpenPage()
