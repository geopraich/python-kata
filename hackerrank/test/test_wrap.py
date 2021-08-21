import pytest
import string
from hackerrank.wrap import wrap


def check_wrap(value, value2, actual):
    result = wrap(value, value2)
    assert result == actual, f"expected; {actual}, got: {result}"


def test_returns_wrapped_text_to_width():
    check_wrap(string.ascii_lowercase, 4, ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx', 'yz'])


if __name__ == '__main__':
    pytest.main()
