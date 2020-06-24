import unittest
from more_fun_with_collections import set_membership

class test_in_set_true( unittest.TestCase ):
    def test_something(self):
        self.assertEqual(set_membership.in_set(mySet, 4), True)

    def test_in_set_true(self):
        self.assertEqual(set_membership.in_set(mySet, 7), False)


mySet = set([4,3,2,1])

if __name__ == '__main__':
    unittest.main()
