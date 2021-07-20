def solution(n, works):
    global total
    N = len(works)
    while True:
        if any(works) and n:
            for i in range(N):
                if works[i] == max(works):
                    works[i] -= 1
                    n -= 1
                    if not n:
                        break
        else:
            break

    for work in works:
        total += work**2
    return total




