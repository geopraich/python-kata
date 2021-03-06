import unittest
from hackerrank.findpercentage import find_percentage


class FindPercentageTestCase(unittest.TestCase):
    def test_find_percentage_Malika(self):
        result = find_percentage({"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}, "Malika")
        self.assertEqual(result, format(56.00, ".02f"), f"expected {56.00:.02f}: actual {result}")

    def test_find_percentage_Arjun(self):
        result = find_percentage({"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}, "Arjun")
        self.assertEqual(result, format(77.00, ".02f"), f"expected {77.00:.02f}: actual {result}")


if __name__ == '__main__':
    unittest.main()
