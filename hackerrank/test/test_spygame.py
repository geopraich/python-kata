import unittest
from hackerrank.spygame import spy_game


class SpyGameTestCase1(unittest.TestCase):
    def test_spy_game_True(self):
        result = spy_game([0, 2, 3, 4, 0, 3, 7])
        self.assertEqual(result, True, f"expected: True actual: {result}")

    def test_spy_game_False(self):
        result = spy_game([0, 2, 3, 4, 3, 7, 0])
        self.assertEqual(result, False, f"expected: False actual: {result}")

    def test_spy_game_False_one(self):
        result = spy_game([0, 2, 3, 4, 3, 7])
        self.assertEqual(result, False, f"expected: False actual: {result}")

    def test_spy_game_False_two(self):
        result = spy_game([7, 0, 0, 4, 3])
        self.assertEqual(result, False, f"expected: False actual: {result}")

    def test_spy_game_True_two(self):
        result = spy_game([1, 0, 0, 7])
        self.assertEqual(result, True, f"expected: True actual: {result}")


if __name__ == '__main__':
    unittest.main()
