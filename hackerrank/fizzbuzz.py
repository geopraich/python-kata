def fizz_buzz(nums):
    if nums % 15 == 0:
        return "FizzBuzz"
    elif nums % 3 == 0:
        return "Fizz"
    elif nums % 5 == 0:
        return "Buzz"

    return int(nums)
