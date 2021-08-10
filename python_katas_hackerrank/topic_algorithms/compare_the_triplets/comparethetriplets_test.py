import unittest
from comparethetriplets import compare_triplets


class CompareTheTripletsTestCase1(unittest.TestCase):
    def test_compare_triplets(self):
        result = compare_triplets([5, 6, 7], [3, 6, 10])
        self.assertEqual(result, [1, 1])


class CompareTheTripletsTestCase2(unittest.TestCase):
    def test_compare_triplets(self):
        result = compare_triplets([17, 28, 30], [99, 16, 8])
        self.assertEqual(result, [2, 1])


if __name__ == '__main__':
    unittest.main()
