def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if score3 < 0:
        raise (ValueError)
        return float((score1 + score2 + score3)/NUMBER_TESTS)



