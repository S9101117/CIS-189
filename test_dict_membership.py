import unittest
from more_fun_with_collections import dict_membership

class test_in_set_true( unittest.TestCase ):
    def test_something(self):
        self.assertEqual(dict_membership.in_dict(mySet, 4), True)

    def test_in_set_true(self):
        self.assertEqual(dict_membership.in_dict(mySet, 8), False)

mySet = set([4,3,2,1])


if __name__ == '__main__':
    unittest.main()
