import pytest
from data import url_main_page, order_data_set_1, order_data_set_2
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


class TestOrderPage(OrderPage):

    @pytest.mark.parametrize(
        "button_locator, order_data",
        [
            (MainPageLocators.BUTTON_HEADER_ORDER, data.order_data_set_1),
            (MainPageLocators.BUTTON_FOOTER_ORDER, data.order_data_set_2),
        ],
    )
    def test_question_answer(self, driver, num_of_qa, button_locator, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_url(url_main_page)
        main_page.click_on_button(button_locator)
        order_page.fill_order_form(order_data)
        assert main_page.check_text_answer(num_of_qa, answer_texts[num_of_qa])
