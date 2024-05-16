from selene import browser


class OpenPage:

    def open_start_page(self):
        browser.open('/')
        return self

    def open_knowledge_base(self):
        browser.element('a[href="https://help.telega.in/hc/ru"]').click()
        return self

    def open_registration_form(self):
        browser.element('div[class="btn blue hover-orange js_open_registration"]').click()
        return self

    def open_login_form(self):
        browser.element('div[class="enter js_login cursor-pointer"]').element('span').click()
        return self

    def open_analytics(self):
        browser.open('/analytics')
        return self
