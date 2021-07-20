


def solution(clothes):
    outfit = dict()
    for cloth in clothes:
        if cloth[1] in outfit:
            outfit[cloth[1]] += 1
        else:
            outfit[cloth] = 1
    total = 1
    for val in outfit.values():
        total *= val+1
    return total - 1



