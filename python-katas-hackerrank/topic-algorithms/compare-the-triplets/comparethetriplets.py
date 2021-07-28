def compare_triplets(a, b,):
    b_score = 0
    a_score = 0
    for num_in_a, num_in_b in zip(a, b):
        if num_in_a == num_in_b:
            pass
        elif num_in_a < num_in_b:
            b_score += 1
        else:
            a_score += 1
    result_list = [a_score, b_score]
    return result_list
