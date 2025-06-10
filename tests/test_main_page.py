import pytest
from data import answer_texts, url_main_page
from pages.main_page import MainPage

class TestMainPage:

    @pytest.mark.parametrize("num_of_qa", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_answer(self, driver, num_of_qa):
        main_page = MainPage(driver)
        main_page.go_to_url(url_main_page)
        assert main_page.check_text_answer(num_of_qa, answer_texts[num_of_qa])
