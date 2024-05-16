import time

from selene import browser, have


class Register:

    def fill_form(self):
        browser.element('#add_user_mail').type('123')
        browser.element('input[name="user[contact]"').type('1234')
        browser.element('#user_register_news_subscription').click()
        browser.element('#sign_up_submit_button').click()
        time.sleep(10)

    def check_reg_error(self):
        browser.element('div[class="error_wrapper mb-4px"]').should(have.text("Введите email в правильном формате"))
