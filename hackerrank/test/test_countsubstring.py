import pytest
from hackerrank.countsubstring import count_substring


def check_count_substring(value_one, value_two, actual):
    result = count_substring(value_one, value_two)
    assert result == actual, f"expected: {actual}, got: {result}"


def test_total_substring_count_same_returns_two():
    check_count_substring('ABCDCDC', 'CDC', 2)


def test_total_substring_count_mix_returns_three():
    check_count_substring('abHeHbhehHeHeHd', 'HeH', 3)


if __name__ == '__main__':
    pytest.main()
