import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from helper_data.data import QuestionsList, Urls
from locators.home_page_locators import HomePageLocators
from locators.yandex_dzen_locators import YandexDzenLocators
from pages.home_scooter_page import HomePage
from pages.yandex_dzen_page import DzenPage


class TestMainPage:
    @allure.title('Test "Click on Scooter logo lead to Scooter main page"')
    @allure.description('''1)Click on "Order" button
                        2)Click on "Scooter" logo
                        3)Compare the expected and current URLs and confirm that the text "Training Simulator" appears''')
    def test_click_on_scooter_logo(self, driver):
        main_page = HomePage(driver)
        main_page.order_button_click()
        main_page.scooter_logo_click()
        current_url = main_page.get_current_url()
        title_displayed = main_page.check_main_title()
        assert current_url == Urls.BASE_SCOOTER_URL and title_displayed

    @allure.title('Test "Click on Yandex logo lead to Yandex Dzen main page"')
    @allure.description('''1)Click on "Yandex" logo
                        2)Switch to new browser tab
                        3)Comparing expected and current URL's and confirm "Main" button appears''')
    def test_click_on_yandex_logo(self, driver):
        main_page = HomePage(driver)
        dzen_page = DzenPage(driver)
        main_page.yandex_logo_click()
        main_page.switch_to_the_new_tab()
        WebDriverWait(driver,5).until(ec.url_to_be(Urls.YA_DZEN_URL))
        assert dzen_page.check_element_main_button

    @allure.title('Test "Answers to FAQ compares to expected answers text"')
    @allure.description('''1)Scroll to FAQ;
                        2)Click on question;
                        3)Get the text of the answers;
                        4)Comparing expected and actual text''')
    @pytest.mark.parametrize('questions_buts_locators, questions_text_locators, expected_question_text', zip(HomePageLocators.questions_buts_locators, HomePageLocators.questions_text_locators, QuestionsList.expected_question_text))
    def test_questions_accordeon(self, driver, questions_buts_locators, questions_text_locators, expected_question_text):
        home_page = HomePage(driver)
        home_page.accept_cookie()
        home_page.scroll_to_questions()
        text = home_page.get_text_of_questions(questions_buts_locators, questions_text_locators)
        assert text == expected_question_text
