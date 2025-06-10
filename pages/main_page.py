from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_on_question(self, num_of_qa):
        self.scroll_to_element(MainPageLocators.QUESTION_TO_SCROLL_XPATH)
        formated_locator = self.format_locator(
            MainPageLocators.QUESTION_XPATH, num_of_qa
        )
        self.click_element(formated_locator)

    def get_answer_text(self, num_of_qa):
        formated_locator = self.format_locator(MainPageLocators.ANSWER_XPATH, num_of_qa)
        return self.get_element_text(formated_locator)

    def check_text_answer(self, num_of_qa, text):
        self.click_on_question(num_of_qa)
        return self.get_answer_text(num_of_qa) == text
