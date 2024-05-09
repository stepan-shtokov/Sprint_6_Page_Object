import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Click on Yandex logo')
    def yandex_logo_click(self):
        self.click_on_button(HomePageLocators.yandex_logo_button)

    @allure.step('Click on Scooter logo')
    def scooter_logo_click(self):
        self.click_on_button(HomePageLocators.scooter_logo_button)

    @allure.step('Click on "Order" header button')
    def order_button_click(self):
        self.click_on_button(HomePageLocators.order_button_from_header)

    @allure.step('Check for "Training simulator" text on header')
    def check_main_title(self):
        return self.wait_about_element_located(HomePageLocators.scooter_logo_text).is_displayed()

    @allure.step('Click on "Accept cookies" button')
    def accept_cookie(self):
        self.wait_about_element_located(HomePageLocators.accept_cookie_button)
        self.click_on_button(HomePageLocators.accept_cookie_button)

    @allure.step('Click "Order" button from page')
    def order_from_another_button(self):
        self.scroll_to_locator(HomePageLocators.order_button_from_page)
        self.check_element_displayed(HomePageLocators.order_button_from_page)
        self.click_on_button(HomePageLocators.order_button_from_page)

    @allure.step('Scroll to FAQ list')
    def scroll_to_questions(self):
        self.scroll_to_locator(HomePageLocators.question_list)

    @allure.step('Click on questions from FAQ list')
    def click_on_questions(self, question_buts_locators):
        self.wait_about_element_located(question_buts_locators)
        self.click_on_button(question_buts_locators)

    @allure.step('Get answers text from FAQ list')
    def get_text_of_questions(self, questions_buts_locators, questions_text_locators):
        self.click_on_questions(questions_buts_locators)
        self.check_element_displayed(questions_text_locators)
        text_of_questions = self.get_text_from_locator(questions_text_locators)
        return text_of_questions
    