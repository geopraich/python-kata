def hackerrank_string(s):
    code = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 1]

    for letter in s:
        if letter == code[0]:
            code.pop(0)
        else:
            pass

    if len(code) == 1:
        return 'YES'

    return 'NO'

