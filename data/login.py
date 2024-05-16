from selene import browser, have


class Login:

    def submit_form(self):
        browser.element('div[class="btn blue hover-orange text_center js_sign_in_submit_button"]').click()

    def check_login_error(self):
        browser.element('div[class="error_wrapper"]').should(have.text("Неверный логин или пароль"))
