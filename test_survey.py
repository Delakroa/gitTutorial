import unittest
from language_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов."""
        question = "На каком языке вы впервые научились говорить?"
        self.my_survey = AnonymousSurvey(question)   # 1
        self.responses = ['English', 'Spanish', 'Mandarin']   # 2

    def test_store_single(self):
        """Проверяет что один ответ сохранён правильно"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
