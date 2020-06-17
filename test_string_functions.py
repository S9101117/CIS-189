import unittest
from more_functions import string_functions

class MyTestCase( unittest.TestCase ):
    def test_multiple_string(self):
        fav_class = str(input("enter favorite class here:"))
        number = int(input("enter n here:"))
        self.assertEqual(string_functions.multiply_string(fav_class,number),fav_class*number)


if __name__ == '__main__':
    unittest.main()
