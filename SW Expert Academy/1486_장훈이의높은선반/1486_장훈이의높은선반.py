def func(n,k):
    global best
    if n == k:
        s = 0
        for i in range(N):
            if L[i]:
                s += heights[i]

        if B <= s < best:
            best = s
    else:
        L[n] = 0
        func(n+1, k)
        L[n] = 1
        func(n+1,k)

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    best = sum(heights)

    L = [0]*N

    func(0, N)
    print('#{} {}'.format(t, best-B))



