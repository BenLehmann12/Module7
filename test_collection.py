import unittest
from unittest.mock import patch
import fun_with_collections.collections as collections


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.collections.get_input', return_value='5')
    def test_something(self,input):
        self.assertEqual(collections.make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
