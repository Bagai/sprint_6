from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    @allure.step("Зааполнение формы заказа первая часть")
    def fill_order_form_part_1(self, order_data):
        self.add_text_to_element(OrderPageLocators.NAME_INPUT_XPATH, order_data["name"])
        self.add_text_to_element(
            OrderPageLocators.SURNAME_INPUT_XPATH, order_data["surname"]
        )
        self.add_text_to_element(
            OrderPageLocators.ADDRESS_INPUT_XPATH, order_data["address"]
        )
        self.click_element(OrderPageLocators.INPUT_METRO_STATION_XPATH)
        self.click_element(OrderPageLocators.METRO_STATION_XPATH)
        self.add_text_to_element(
            OrderPageLocators.PHONE_INPUT_XPATH, order_data["phone"]
        )

    @allure.step("Зааполнение формы заказа вторая часть")
    def fill_order_form_part_2(self, order_data):
        self.add_text_to_element(OrderPageLocators.DATE_XPATH, order_data["date"])
        self.click_element(OrderPageLocators.DATE_CLICK_XPATH)
        self.click_element(OrderPageLocators.DURATION_XPATH)
        self.click_element(OrderPageLocators.SET_DURATION_XPATH)
        self.click_element(OrderPageLocators.COLOR_XPATH)
        self.add_text_to_element(OrderPageLocators.COMMENT_XPATH, order_data["comment"])

    @allure.step("Зааполнение формы заказа (все шаги)")
    def fill_order_form(self, order_data):
        self.fill_order_form_part_1(order_data)
        self.click_element(OrderPageLocators.NEXT_ORDER_BUTTON_XPATH)
        self.fill_order_form_part_2(order_data)

    @allure.step("Нажатие на кнопку заказать")
    def set_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_XPATH)

    @allure.step("Нажатие на кнопку подтверждения заказа")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON_XPATH)

    @allure.step("Проверка модального окна подтверждения заказа")
    def confirm_order_modal(self):
        return self.find_element_with_wait(
            OrderPageLocators.CONFIRMATION_MODAL_XPATH
        ).is_displayed()
