import allure

from data.login import Login
from model.pages.open_page import OpenPage


def test_login():
    page = OpenPage()

    with allure.step("Открывается стартовая страница"):
        page.open_start_page()

    with allure.step("Открывается форма входа"):
        page.open_login_form()

    login = Login()

    with allure.step("Попытка отправить форму с пустыми данными"):
        login.submit_form()

    with allure.step("Нельзя отправить форму с пустыми данными"):
        login.check_login_error()
