T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    C = [0]*(1<<N)
    cnt = 0
    for i in range(1, 1<<N):
        B = []
        for j in range(N+1):
            if i & (1<<j):
                B.append(A[j])
        if sum(B) == K:
            cnt += 1

    print("#{} {}".format(t, cnt))
