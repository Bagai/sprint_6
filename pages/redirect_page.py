from .base_page import BasePage
from locators.redirect_page_locators import RedirectPageLocators
import allure

class RedirectPage(BasePage):

    @allure.step("Нажатие по логотипу Яндекс")
    def click_logo_yandex(self):
        self.click_element(RedirectPageLocators.LOGO_YANDEX_XPATH)

    @allure.step("Нажатие по логотипу Самокат")
    def click_logo_scooter(self):
        self.click_element(RedirectPageLocators.LOGO_SCOOTER_XPATH)

    @allure.step("Проверка открытия страницы Яндекс Дзен")
    def check_dzen_page_opens(self):
        return self.check_element_is_displayed(
            RedirectPageLocators.BUTTON_DZEN_FIND_XPATH
        )

    @allure.step("Проверка открытия страницы Самокат")
    def check_scooter_page_opens(self):
        return self.check_element_is_displayed(RedirectPageLocators.IMG_SCOOTER_XPATH)

    @allure.step("Открытие последнего открытого вкладки")
    def open_last_tab(self):
        self.driver.implicitly_wait(1)
        return super().open_last_tab()
