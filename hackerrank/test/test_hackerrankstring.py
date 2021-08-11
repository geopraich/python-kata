import unittest
from hackerrank.hackerrankstring import hackerrank_string


class HackerRankStringTestCase(unittest.TestCase):
    def test_hackerrank_string_YES(self):
        result = hackerrank_string('hereiamstackerrank')
        self.assertEqual(result, 'YES')

    def test_hackerrank_string_NO(self):
        result = hackerrank_string('hackerworld')
        self.assertEqual(result, 'NO')

    def test_hackerrank_string_long_YES(self):
        result = hackerrank_string('hhaacckkekraraannk')
        self.assertEqual(result, 'YES')

    def test_hackerrank_string_long_NO(self):
        result = hackerrank_string('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt')
        self.assertEqual(result, 'NO')


if __name__ == '__main__':
    unittest.main()
