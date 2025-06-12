from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Нажатие на вопрос {num_of_qa}")
    def click_on_question(self, num_of_qa):
        self.scroll_to_element(MainPageLocators.QUESTION_TO_SCROLL_XPATH)
        formated_locator = self.format_locator(
            MainPageLocators.QUESTION_XPATH, num_of_qa
        )
        self.click_element(formated_locator)

    @allure.step("Получение текста ответа на вопрос {num_of_qa}")
    def get_answer_text(self, num_of_qa):
        formated_locator = self.format_locator(MainPageLocators.ANSWER_XPATH, num_of_qa)
        return self.get_element_text(formated_locator)

    @allure.step("Проверка текста ответа на вопрос {num_of_qa}")
    def check_text_answer(self, num_of_qa, text):
        self.click_on_question(num_of_qa)
        return self.get_answer_text(num_of_qa) == text

    @allure.step("Нажатие на кнопку заказа")
    def click_on_button_order(self, locator):
        self.click_element(locator)

    @allure.step("Скролл до кнопки заказа")
    def scroll_to_element(self, locator):
        return super().scroll_to_element(locator)
