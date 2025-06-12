import pytest
from data import url_main_page, order_data_set_1, order_data_set_2
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


class TestOrderPage:

    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.BUTTON_HEADER_ORDER, order_data_set_1),
            (MainPageLocators.BUTTON_FOOTER_ORDER, order_data_set_2),
        ],
    )
    def test_creation_order(self, driver, button_locator, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_url(url_main_page)
        main_page.scroll_to_element(button_locator)
        main_page.click_on_button_order(button_locator)
        order_page.fill_order_form(order_data)
        order_page.set_order()
        order_page.confirm_order()
        assert order_page.confirm_order_modal()
