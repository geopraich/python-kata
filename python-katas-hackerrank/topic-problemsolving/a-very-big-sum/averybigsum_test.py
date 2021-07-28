import unittest
from averybigsum import a_very_big_sum


class AVeryBigSumTestCase(unittest.TestCase):
    def test_a_very_big_sum(self):
        result = a_very_big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
        self.assertEqual(result, int(5000000015))


if __name__ == '__main__':
    unittest.main()
