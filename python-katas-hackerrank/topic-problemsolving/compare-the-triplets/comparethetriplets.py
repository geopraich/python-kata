def compare_triplets(a, b):
    bscore = 0
    ascore = 0
    for numina, numinb in zip(a, b):
        if numina == numinb:
            pass
        elif numina < numinb:
            bscore += 1
        else:
            ascore += 1
    resultlist = [ascore, bscore]
    return resultlist
