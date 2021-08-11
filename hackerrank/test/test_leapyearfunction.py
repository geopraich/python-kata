import unittest
from hackerrank.leapyearfunction import find_leap_year


class LeapYearFunctionTestCase1(unittest.TestCase):
    def test_find_leap_year(self):
        result = find_leap_year(1990)
        self.assertEqual(result, False, f"expected False: actual {result}")


class LeapYearFunctionTestCase2(unittest.TestCase):
    def test_find_leap_year(self):
        result = find_leap_year(1984)
        self.assertEqual(result, True, f"expected True: actual {result}")


class LeapYearFunctionTestCase3(unittest.TestCase):
    def test_find_leap_year(self):
        result = find_leap_year(2000)
        self.assertEqual(result, True, f"expected True: actual {result}")


class LeapYearFunctionTestCase4(unittest.TestCase):
    def test_find_leap_year(self):
        result = find_leap_year(1900)
        self.assertEqual(result, False, f"expected False: actual {result}")


if __name__ == '__main__':
    unittest.main()
