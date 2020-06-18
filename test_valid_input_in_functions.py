import unittest
from more_functions import validate_input_in_functions

class MyTestCase( unittest.TestCase ):
    def test_score_input_test_name(self):
        self.assertEqual(validate_input_in_functions.score_input(test_name= "Saad"), Saad , 0)

    def test_score_input_test_score_valid(self):
        self.assertEqual(validate_input_in_functions.score_input(test_name="Saad",test_score=55), Saad , 55)

    def test_score_input_test_score_below_range(self):
        self.assertEqual(validate_input_in_functions.score_input(test_name="Saad",test_score=-79),'Invalid test score, try again Please enter a number between 0-100')

    def test_score_input_test_score_above_range(self):
        self.assertEqual(validate_input_in_functions.score_input(test_name="Saad",test_score=-79),'Invalid test score, try again Please enter a number between 0-100')

   # def test_test_score_non_numeric(self):
       # self.assertEqual(validate_input_in_functions.score_input(test_name="Saad",test_score=CS),'NameError: name 'pp' is not defined')

    def test_score_input_invalid_message(self):
        self.assertEqual(validate_input_in_functions.score_input("Saad", test_score=90, invalid_message="Invalid test score, try again "), Saad , 90)








if __name__ == '__main__':
    unittest.main()
