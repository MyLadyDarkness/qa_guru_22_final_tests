import allure
from selene import browser, have


class Login:

    def submit_form(self):
        with allure.step("Попытка отправить форму с пустыми данными"):
            browser.element('.btn.js_sign_in_submit_button').click()

    def check_login_error(self):
        with allure.step("Нельзя отправить форму с пустыми данными"):
            #browser.element('[class="error_wrapper"]').should(have.text("Неверный логин или пароль"))
            browser.element('.input_auth_code').element('.error_wrapper').should(have.text("Неверный логин или пароль"))


#input_auth_code

login = Login()
