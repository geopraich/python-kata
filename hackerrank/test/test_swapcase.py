import pytest
from hackerrank.swapcase import swap_case


def check_swap_case(value, actual):
    result = swap_case(value)
    assert result == actual, f"expected: {actual}, got: {result}"


def test_returns_a_uppercase_when_lowercase_char_passed_in():
    check_swap_case("a", "A")


def test_returns_a_lowercase_char_when_uppercase_char_passed_in():
    check_swap_case("A", "a")


def test_returns_all_cases_swapped_when_string_passed_in():
    check_swap_case("HackerRank.com presents 'Pythonist 2'.", "hACKERrANK.COM PRESENTS 'pYTHONIST 2'.")


if __name__ == '__main__':
    pytest.main()
