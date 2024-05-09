import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Send name to name input field')
    def send_name_to_name_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.name_input_field, text)

    @allure.step('Send last name to last name input field')
    def send_last_name_to_last_name_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.last_name_input_field, text)

    @allure.step('send delivery address to delivery address field')
    def send_address_to_address_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.address_input_field, text)

    @allure.step('Send subway station to subway station input field')
    def send_subway_to_subway_input(self, text):
        self.click_on_button(OrderPageLocators.subway_station_input_field)
        self.send_keys_to_fields(OrderPageLocators.subway_station_input_field, text)
        self.click_on_button(OrderPageLocators.subway_after_choose_field)

    @allure.step('Send phone number to telephone input field')
    def send_phone_number_to_number_input_field(self, text):
        self.send_keys_to_fields(OrderPageLocators.phone_number_input_field, text)

    @allure.step('Click on "Proceed" button in order form')
    def click_on_next_button(self):
        self.click_on_button(OrderPageLocators.proceed_button)

    @allure.step('Completely fill first part of order form')
    def fill_order_form_for_who(self, user_1):
        self.send_name_to_name_input(user_1[1])
        self.send_last_name_to_last_name_input(user_1[2])
        self.send_address_to_address_input(user_1[3])
        self.send_subway_to_subway_input(user_1[4])
        self.send_phone_number_to_number_input_field(user_1[5])
        self.click_on_next_button()

    @allure.step('Send scooter delivery date to input field')
    def send_deliver_date_to_delivery_input(self, text):
        self.click_on_button(OrderPageLocators.time_of_deliver_field)
        self.send_keys_to_fields(OrderPageLocators.time_of_deliver_field, text)

    @allure.step('Choose rent time')
    def rent_time_choose(self):
        self.click_on_button(OrderPageLocators.rent_time_field)
        self.click_on_button(OrderPageLocators.rent_time_after_choose)

    @allure.step('Choose gray scooter colour')
    def scooter_colour_choose(self):
        self.click_on_button(OrderPageLocators.scooter_colour_check_gray)

    @allure.step('Send comment to comment input field')
    def send_comment_to_comment_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.comment_for_courier_field, text)

    @allure.step('Click on "Order" button to finish order process')
    def finish_order(self):
        self.click_on_button(OrderPageLocators.order_button)

    @allure.step('Completely fill second part of order form')
    def complete_filling_of_order_form(self, text):
        self.send_deliver_date_to_delivery_input(text[6])
        self.rent_time_choose()
        self.scooter_colour_choose()
        self.send_comment_to_comment_input(text[7])
        self.finish_order()

    @allure.step('Order confirmation')
    def confirm_order(self):
        self.click_on_button(OrderPageLocators.yes_button)

    @allure.step('Complete work-flow of an order')
    def full_flow_to_order(self, user_1):
        self.fill_order_form_for_who(user_1)
        self.complete_filling_of_order_form(user_1)
        self.confirm_order()

    @allure.step('Order checkout popup window')
    def order_completed_popup(self):
        return self.wait_about_element_located(OrderPageLocators.order_completed_popup).is_displayed()
