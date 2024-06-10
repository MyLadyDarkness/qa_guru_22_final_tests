import allure
from selene import browser, have


class HotOffers:
    def load_more(self):
        with allure.step("Загрузить больше горячих предложений"):
            browser.element('.btn_b').element('.btn_load_more_hot_offers').click()
        return self

    def check_loaded(self):
        with allure.step("Проверить, что загруженные предложения отобразились"):
            browser.element('.hidden_offers[style]').should(have.attribute('style'))
        return self


hot_offers = HotOffers()
