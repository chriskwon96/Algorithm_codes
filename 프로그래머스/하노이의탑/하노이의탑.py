def hanoi(n, start, to, via):
    if n == 1:
        ans.append([start, to])
    else:
        hanoi(n-1, start, via, to)
        ans.append([start, to])
        hanoi(n-1, via, to, start)


def solution(n):
    global ans
    ans = []
    hanoi(n,1,3,2)

    return ans

solution(2)

