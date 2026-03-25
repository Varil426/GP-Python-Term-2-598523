from io import StringIO
from unittest.mock import patch

import funkcje
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(funkcje.add(2,4), 6)
        self.assertNotEqual(funkcje.add(2,4), 5)

class TestDivideFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_divide(self, mock_stdout):
        funkcje.divide(4,2)
        self.assertEqual(mock_stdout.getvalue(), "2.0\n")

if __name__ == "__main__":
    unittest.main()