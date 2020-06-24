import unittest
from fun_with_collections import sort_and_search_array

class MyTestCase( unittest.TestCase ):
    def test_item_found(self):
        self.assertEqual(sort_and_search_array.search_array(anyList,6), 2)


    def test_item_not_found(self):
        self.assertEqual(sort_and_search_array.search_array(anyList,33), -1)

    def test_sort_list(self):
        self.assertEqual(sort_and_search_array.sort_array(anyList),[1, 2, 3, 4, 5, 6, 7, 8])

anyList = [5,4,6,3,7,2,8,1]


if __name__ == '__main__':
    unittest.main()
