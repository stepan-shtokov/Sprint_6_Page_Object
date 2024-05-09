from helper_data.data import Users
from pages.home_scooter_page import HomePage
from pages.order_scooter_page import OrderPage
import allure


class TestOrderPage:
    @allure.title('Test "Order by header button"')
    @allure.description('''1)Clicking on header "Order" button;
                        2)Filling first part of an order form;
                        3)Filling second part of an order form;
                        4)Confirming order;
                        5)Waiting for order confirmation popup being displayed''')
    def test_order_by_header_button(self, driver):
        main_page = HomePage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.order_button_click()
        order_page.full_flow_to_order(Users.user_1)
        assert order_page.order_completed_popup()

    @allure.title('Test "Order by page button"')
    @allure.description('''1)Clicking on page "Order" button;
                        2)Filling first part of an order form;
                        3)Filling second part of an order form;
                        4)Confirming order;
                        5)Waiting for order confirmation popup being displayed''')
    def test_order_by_page_button(self, driver):
        main_page = HomePage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.order_from_another_button()
        order_page.full_flow_to_order(Users.user_2)
        assert order_page.order_completed_popup()
