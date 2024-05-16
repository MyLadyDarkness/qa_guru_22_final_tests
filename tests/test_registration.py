import allure

from data.register import Register
from model.pages.open_page import OpenPage


def test_registration():
    page = OpenPage()

    with allure.step("Открывается стартовая страница"):
        page.open_start_page()

    with allure.step("Открывается форма входа"):
        page.open_registration_form()

    registration = Register()

    with allure.step("Ввод данных"):
        registration.fill_form()

    with allure.step("Нельзя зарегистрироваться с неправильным email"):
        registration.check_reg_error()
