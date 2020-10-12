import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for AnonymousSurvey class"""

    def setUp(self) -> None:
        question = "What is your native language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['polish', 'english', 'spanish']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest

