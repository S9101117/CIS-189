import unittest
from unittest.mock import patch
from fun_with_collections import basic_list_exception


class TestList(unittest.TestCase):
    @patch( "fun_with_collections.basic_list_exception.get_input", return_value='6' )
    def test_make_list(self, input):
        self.assertEqual(basic_list_exception.make_list(), ['6', '6', '6'])

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):          # this is familiar
            basic_list_exception.make_list()




    @patch('fun_with_collections.basic_list_exception.get_input', return_value='-2')  # patch function for input
    def test_make_list_below_range(self, input):                        # pass input
        with self.assertRaises(ValueError):          # this is familiar
            basic_list_exception.make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='56')  # patch function for input
    def  test_make_list_above_range(self, input):                        # pass input
        with self.assertRaises(ValueError):          # this is familiar
            basic_list_exception.make_list()



if __name__ == '__main__':
    unittest.main()
