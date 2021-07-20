from itertools import combinations


def solution(number,k):
    number = list(number)
    combs = list(combinations(range(len(number)), k))
    max_num = 0
    for comb in combs:
        new = number[::]
        for c in comb:
            new[c] = ""
        # print(int("".join(new)))
        if max_num < int("".join(new)):
            max_num = int("".join(new))
    return str(max_num)


