import unittest
from pythonifelsechallenge import find_odd

class FindOddTestCase(unittest.TestCase):
    def test_find_odd(self):
        result = find_odd(3)
        self.assertEqual(result,"Weird", f"Should be Weird actual is {result}")


class FindOddTestCase2(unittest.TestCase):
    def test_find_odd(self):
        result = find_odd(24)
        self.assertEqual(result,"Not Weird", f"Should be Not Weird actual is {result}")


if __name__ == '__main__':
    unittest.main()
