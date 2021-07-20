from math import gcd


def solution(w,h):
    return w*h - (w+h-gcd(w,h))



print(solution(8,12))
print(solution(2,2))
print(solution(1,1))
print(solution(3,4))