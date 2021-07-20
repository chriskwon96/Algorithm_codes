import math


def solution(n, stations, w):
    ans = 0

    if stations[0] > w+1 :
        space = stations[0] - (w+1)
        ans += math.ceil(space / (2 * w + 1))


    if n - stations[-1] > w:
        space = n-stations[-1]-w
        ans += math.ceil(space / (2 * w + 1))


    for i in range(len(stations)-1):
        if stations[i+1]-stations[i]-1 > 2*w:
            space = (stations[i+1]-w)-(stations[i]+w)-1
            ans += math.ceil(space / (2 * w + 1))


    return ans

#
#
# n = 11
# stations=[4, 11]
# w = 1
#
# # n = 16
# # stations = [9]
# # w = 2

print(solution(n, stations, w))






