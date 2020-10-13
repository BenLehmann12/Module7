import unittest
from unittest.mock import patch
from fun_with_collections import list_exception as exception

class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.exception.get_input',return_value='ab')
    def test_something(self,input):
        with self.assertRaises(ValueError):
            exception.make_list()


if __name__ == '__main__':
    unittest.main()
