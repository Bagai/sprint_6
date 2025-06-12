from data import url_order_page, url_main_page
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.redirect_page import RedirectPage


class TestRedirectPage:

    def test_click_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_url(url_order_page)
        redirect_page = RedirectPage(driver)
        redirect_page.click_logo_scooter()
        assert redirect_page.check_scooter_page_opens()

    def test_open_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_url(url_main_page)
        redirect_page = RedirectPage(driver)
        redirect_page.click_logo_yandex()
        redirect_page.open_last_tab()
        assert redirect_page.check_dzen_page_opens()
