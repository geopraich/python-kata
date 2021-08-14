import pytest
from hackerrank.splitandjoin import split_and_join


def check_split_and_join(value, actual):
    result = split_and_join(value)
    assert result == actual, f"expected: {actual}, got: {result}"


def test_returns_string_with_hyphens_instead_of_spaces():
    check_split_and_join('this is a string', 'this-is-a-string')


if __name__ == '__main__':
    pytest.main()
