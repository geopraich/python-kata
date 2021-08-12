def list_comprehension_function(x, y, z, n):
    final_lst = [[numx, numy, numz] for numx in range(0, x + 1) for numy in range(0, y + 1) for numz in range(0, z + 1)
                 if numx + numy + numz != n]

    return final_lst
