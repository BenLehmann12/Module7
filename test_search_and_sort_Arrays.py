import unittest
import fun_with_collections.sort_and_search_Array as sort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sort.search_array([2,10,1,6,8,3],1), 2)

    def test_another(self):
        self.assertEqual(sort.search_array([2,10,1,6,8,3],8),4)


if __name__ == '__main__':
    unittest.main()
