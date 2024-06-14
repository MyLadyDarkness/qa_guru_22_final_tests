import allure
from selene import browser, have


@allure.story("Форма регистрации")
class Register:

    def fill_form(self):
        with allure.step("Ввод данных"):
            browser.element('#add_user_mail').type('123')
            browser.element('input[name="user[contact]"').type('1234')
            browser.element('#user_register_news_subscription').click()
            browser.element('#sign_up_submit_button').click()

    def check_reg_error(self):
        with allure.step("Нельзя зарегистрироваться с неправильным email"):
            browser.element('.item.email.error').element('.error_wrapper').should(
                have.text("Введите email в правильном формате"))


registration = Register()
