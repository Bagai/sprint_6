from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def fill_order_form_part_1(self, order_data):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT_XPATH, order_data["name"])
        self.add_text_to_element(
            OrderPageLocators.SURNAME_INPUT_XPATH, order_data["surname"]
        )
        self.add_text_to_element(
            OrderPageLocators.ADDRESS_INPUT_XPATH, order_data["address"]
        )
        self.click_element(OrderPageLocators.INPUT_METRO_STATION_SELECT)
        self.click_element(OrderPageLocators.METRO_STATION_SELECT)
        self.add_text_to_element(
            OrderPageLocators.PHONE_INPUT_XPATH, order_data["phone"]
        )

    def fill_order_form_part_2(self, order_data):
        self.add_text_to_element(OrderPageLocators.DATE_XPATH, order_data["date"])
        self.click_element(OrderPageLocators.INPUT_METRO_STATION_SELECT)
        self.click_element(OrderPageLocators.DURATION_XPATH)
        self.click_element(OrderPageLocators.SET_DURATION_XPATH)
        self.click_element(OrderPageLocators.COLOR_XPATH)
        self.select_option_by_text(
            OrderPageLocators.COMMENT_XPATH, order_data["comment"]
        )

    def fill_order_form(self, order_data):
        self.fill_order_form_part_1(order_data)
        self.fill_order_form_part_2(order_data)
