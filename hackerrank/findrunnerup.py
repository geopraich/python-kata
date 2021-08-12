def find_runner_up(lst):
    lst = list(set(lst))
    lst.sort()

    return lst[len(lst) - 2]
