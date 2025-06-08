import pytest
import conftest
from data import answer_texts

class TestMainPage:
    @pytest.mark.parametrize("num_of_qa", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_answer(self, driver, num_of_qa):
        main_page = conftest.MainPage(driver)
        assert main_page.check_text_answer(num_of_qa, answer_texts[num_of_qa])