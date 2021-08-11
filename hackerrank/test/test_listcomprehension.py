import unittest
from hackerrank.listcomprehension import list_comprehension_function


class ListComprehensionTestCase(unittest.TestCase):
    def test_list_comprehension_function(self):
        result = list_comprehension_function(1, 1, 1, 2)
        self.assertEqual(result, [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
                         f"expected [[0, 0, 0],[0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]: actual {result}")


if __name__ == '__main__':
    unittest.main()
