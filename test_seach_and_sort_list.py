import unittest
from fun_with_collections import lists as list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(list.search_list([9,20,1,16,2],2), 4)

    def test_another(self):
        self.assertEqual(list.search_list([9,20,1,16,2],-20),-1)


if __name__ == '__main__':
    unittest.main()
