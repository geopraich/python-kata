def find_odd(number):
    if number % 2 != 0:
        return "Weird"
    elif number == 2 or number == 4:
        return "Not Weird"
    elif number % 2 == 0:
        if 6 <= number <= 20:
            return "Weird"
        elif number > 20:
            return "Not Weird"
