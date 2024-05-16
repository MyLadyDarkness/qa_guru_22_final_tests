import time

from selene import browser


class OpenPage:

    def open_start_page(self):
        browser.open('/')
        return self

    def open_webmaster_page(self):
        browser.open('/')

        time.sleep(50)
        browser.element('div[class=toggle-checkbox]').click()

        return self

    def open_knowledge_base(self):
        browser.element('a[href="https://help.telega.in/hc/ru"]').click()
        browser.element(
            'a[href="/hc/ru/categories/4417847105553--%D0%91%D0%90%D0%97%D0%90-%D0%97%D0%9D%D0%90%D0%9D%D0%98%D0%99"]').click()
        return self

    def open_registration_form(self):
        browser.element('div[class="btn blue hover-orange js_open_registration"]').click()

    def open_login_form(self):
        browser.element('div[class="enter js_login cursor-pointer"]').element('span').click()

    def open_analytics(self):
        browser.open('/analytics')
