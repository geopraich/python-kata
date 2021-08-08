import unittest
from pythonifelsechallenge import find_odd

class FindOddTestCase(unittest.TestCase):
    def test_find_odd(self):
        result = find_odd(3)
        self.assertEqual(result,"Weird", f"expected Weird: actual {result}")


class FindOddTestCase2(unittest.TestCase):
    def test_find_odd(self):
        result = find_odd(24)
        self.assertEqual(result,"Not Weird", f"expected Not Weird: actual {result}")


if __name__ == '__main__':
    unittest.main()
