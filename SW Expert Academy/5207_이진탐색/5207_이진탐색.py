def binsearch(l, r, target, side):
    global cnt
    if l <= r:
        m = (l+r)//2
        if A[m] == target:
            cnt += 1
        else:
            if side != 1 and A[m] < target:
                binsearch(m+1, r, target, 1)
            elif side != 0 and target < A[m]:
                binsearch(l, m-1, target, 0)


T = int(input())
for t in range(1, T+1):
    N,M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(M):
        binsearch(0, N-1, B[i], -1)
    print('#{} {}'.format(t, cnt))
