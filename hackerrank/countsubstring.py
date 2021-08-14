def count_substring(string, sub_string):
    total = 0

    for index, letter in enumerate(string):

        if letter == sub_string[0] and string[index:index + len(sub_string)] == sub_string:
            total += 1
        else:
            continue

    return total
