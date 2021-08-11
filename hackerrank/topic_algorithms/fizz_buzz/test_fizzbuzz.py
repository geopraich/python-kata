import pytest
from fizzbuzz import fizz_buzz


def check_fizz_buzz(value, actual):
    result = fizz_buzz(value)
    assert result == actual


def test_returns_1_when_1_passed_in():
    check_fizz_buzz(1, 1)


def test_return_2_when_2_passed_in():
    check_fizz_buzz(2, 2)


def test_return_fizz_when_3_passed_in():
    check_fizz_buzz(3, "Fizz")


def test_return_buzz_when_5_passed_in():
    check_fizz_buzz(5, "Buzz")


def test_return_fizz_when_6_passed_in():
    check_fizz_buzz(6, "Fizz")


def test_return_buzz_when_10_passed_in():
    check_fizz_buzz(10, "Buzz")


def test_return_fizzbuzz_when_15_passed_in():
    check_fizz_buzz(15, "FizzBuzz")

