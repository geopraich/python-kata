import unittest
from hackerrank.leapyearfunction import find_leap_year


class LeapYearFunctionTestCase1(unittest.TestCase):
    def test_find_leap_year_FALSE(self):
        result = find_leap_year(1990)
        self.assertEqual(result, False, f"expected False: actual {result}")

    def test_find_leap_year_TRUE(self):
        result = find_leap_year(1984)
        self.assertEqual(result, True, f"expected True: actual {result}")

    def test_find_leap_year_alternate_TRUE(self):
        result = find_leap_year(2000)
        self.assertEqual(result, True, f"expected True: actual {result}")

    def test_find_leap_year_alternate_FALSE(self):
        result = find_leap_year(1900)
        self.assertEqual(result, False, f"expected False: actual {result}")


if __name__ == '__main__':
    unittest.main()
