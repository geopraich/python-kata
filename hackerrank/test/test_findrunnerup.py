import unittest
from hackerrank.findrunnerup import find_runner_up


class FindRunnerUpTestCase1(unittest.TestCase):
    def test_find_runner_up(self):
        result = find_runner_up([2, 3, 6, 6, 5])
        self.assertEqual(result, 5, f"expected 5: actual {result}")

    def test_find_runner_up_one(self):
        result = find_runner_up([-10, -3, -6, -1, -5])
        self.assertEqual(result, -3, f"expected -3: actual {result}")

    def test_find_runner_up_two(self):
        result = find_runner_up([-10, 100, 3, 45, -5, 45])
        self.assertEqual(result, 45, f"expected 45: actual {result}")


if __name__ == '__main__':
    unittest.main()
