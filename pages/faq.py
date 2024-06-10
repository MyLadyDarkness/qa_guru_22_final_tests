import allure
from selene import browser, have, by


class Faq:

    def click_faq_item(self):
        with allure.step("Развернуть текст про интеграции"):
            (browser
             .element('.faq-item')
             .element(by.text('Что за интеграции в Telegram?'))
             .element('.keyboard_arrow').click())

        return self

    def check_text(self):
        with allure.step("Проверить, что отображается нужный текст"):
            (browser.element('.faq-item.active>.js_toggle_faq_content').
             should(have.text('Это размещение промо сообщений')))

        return self


faq = Faq()
