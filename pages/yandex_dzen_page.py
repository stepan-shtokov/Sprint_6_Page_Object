import allure
from pages.base_page import BasePage
from locators.yandex_dzen_locators import YandexDzenLocators


class DzenPage(BasePage):
    @allure.step("Check for ""Main"" button being displayed at Yandex. Dzen")
    def check_element_main_button(self):
        self.wait_about_element_located(YandexDzenLocators.dzen_main_page_button)
        self.check_element_displayed(YandexDzenLocators.dzen_main_page_button)
